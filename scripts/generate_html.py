import csv
import sys

def print_html(file_path):
    print_html_pass(file_path, 1)
    print_html_pass(file_path, 2)

def print_html_pass(file_path, pass_num):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Read the header row
        # Check if the header is valid
        expected_header = ["Timestamp", "Name", "Email", "Talk title", "Abstract", "Short bio",
                           "Link to backup video recording", "Link to presentation (PDF)",
                           "Links to related materials (extended version of talk, demo recording etc.)"]
        if header != expected_header:
            print("Invalid CSV format. Please check the header row.")
            return

        if pass_num == 1:
            print("<h2 id=\"schedule\">Workshop schedule</h2>")
            print()  # Print an empty line between entries
            talkCounter = 0
            for row in csv_reader:
                timestamp, name, email, talk_title, abstract, short_bio, video_link, presentation_link, related_links = row
                # Perform desired operations with the data
                #print("Timestamp:", timestamp)
                line = "<p>"
                if timestamp:
                    talkCounter = talkCounter + 1
                    line = line + f"<a href=\"#t{talkCounter}\">"
                #print(f"{name}")
                #print("Email:", email)
                #print("Talk Title:", talk_title)
                line = line + talk_title + " " + name
                if timestamp:
                    line = line + f"</a>"
                line = line + "</p>"
                print(line)
                #print("Abstract:", abstract)
                #print("Short Bio:", short_bio)
                #print("Video Link:", video_link)
                #print("Presentation Link:", presentation_link)
                #print("Related Links:", related_links)
                print()  # Print an empty line between entries


        elif pass_num == 2:
            print("<h2 id=\"talks\">Talks</h2>")
            print()  # Print an empty line between entries
            talkCounter = 0
            for row in csv_reader:
                timestamp, name, email, talk_title, abstract, short_bio, video_link, presentation_link, related_links = row
                # Perform desired operations with the data
                if not timestamp:
                    continue
                #print("Timestamp:", timestamp)
                line = ""
                talkCounter = talkCounter + 1
                #print("Talk Title:", talk_title)
                line = line + f"<h3 id=\"t{talkCounter}\">{talk_title}</h3>\n"
                #print("Name:", name)
                line = line + f"<p>Presenter: {name}<p>\n"
                #print("Email:", email)
                #print("Abstract:", Abstract)
                line = line + f"<p>Abstract: {abstract}<p>\n"
                #print("Short Bio:", short_bio)
                line = line + f"<p>Bio: {short_bio}<p>\n"
                #print("Video Link:", video_link)
                #print("Presentation Link:", presentation_link)
                if presentation_link:
                  line = line + f"<p>Presentation Link: <a href=\"{presentation_link}\">{presentation_link}</a><p>\n"
                #print("Related Links:", related_links)
                if related_links:
                  line = line + f"<p>Related link: {related_links}<p>\n"
                print(line)
                print()  # Print an empty line between entries
        else:
            print("Invalid pass number:", pass_num)


#process_csv_file("input1.csv")

# Check if the CSV file path is provided as the first argument
if len(sys.argv) < 2:
    print("Please provide the path to the CSV file as the first argument.")
    sys.exit(1)

# Get the CSV file path from the command-line argument
csv_file_path = sys.argv[1]

# Call the function to read the CSV file
print_html(csv_file_path)
