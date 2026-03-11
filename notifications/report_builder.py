def build_email_table(posts, title):

    rows = ""

    for p in posts:

        rows += f"""
        <tr>
            <td>{p['posted_at']}</td>
            <td>{p['post_text']}</td>
            <td><a href="{p['post_url']}">View Post</a></td>
        </tr>
        """

    html = f"""
    <html>
    <body>

    <h2>{title}</h2>

    <table border="1" cellspacing="0" cellpadding="8">

        <tr>
            <th>Timestamp</th>
            <th>Post Content</th>
            <th>Link</th>
        </tr>

        {rows}

    </table>

    </body>
    </html>
    """

    return html