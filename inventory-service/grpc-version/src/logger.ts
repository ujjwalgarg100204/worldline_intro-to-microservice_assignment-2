import { createLogger, format, transports } from "winston";

const logger = createLogger({
  level: "info", // Set logging level (info, debug, error, etc.)
  format: format.combine(
    format.timestamp(), // Adds timestamp to logs
    format.colorize(), // Adds colors for console output
    format.printf(({ timestamp, level, message }) => {
      return `[${timestamp}] ${level}: ${message}`;
    }),
  ),
  transports: [
    new transports.Console(), // Log to the console
  ],
});

export default logger;
