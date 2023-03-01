/**
 * Connect to redis server via redis client
 */
import { createClient } from "redis";

(async function() {
  const client = createClient();
  client.on('error', err => console.log("Redis client not connected to the server: ", err));
  await client.connect();
  console.log("Redis client connected to the server");
  await client.disconnect()
})();
