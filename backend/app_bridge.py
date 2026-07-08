DB_PATH = "/data/data/com.termux/files/home/projects/matatu-fleet-tracker/database/fleet.db"
import sqlite3
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

DB_PATH = "../database/fleet.db"

class FleetDataBridge(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Only handle requests sent to our vehicles data route
        if self.path == "/api/integration/vehicles":
            try:
                # 1. Connect to our localized database file
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row # Allows us to fetch data as key-value pairs
                cursor = conn.cursor()

                # 2. Join our vehicles and routes tables to calculate operational integrity
                query = """
                    SELECT v.number_plate, v.total_odometer, r.route_number, r.strain_factor 
                    FROM vehicles v
                    JOIN routes r ON v.current_route_id = r.id
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                # 3. Format the data into a clean JSON array for the Frontend React app
                fleet_list = []
                for row in rows:
                    fleet_list.append({
                        "plate": row["number_plate"],
                        "odometer": row["total_odometer"],
                        "route": row["route_number"],
                        "strain": row["strain_factor"]
                    })

                conn.close()

                # 4. Send successful HTTP headers with critical CORS access enabled
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*") # Critical for frontend connection
                self.end_headers()

                # 5. Write out the final data payload
                self.wfile.write(json.dumps(fleet_list).encode())

            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            # Return a 404 error for any other URL path
            self.send_response(404)
            self.end_headers()

print("SaccoSync Integration Engine running on port 8000...")
HTTPServer(("0.0.0.0", 8000), FleetDataBridge).serve_forever()

