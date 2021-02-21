from spotify import get_track_info
from slack import set_user_status


def main():
    """Application entrypoint. If there is song currently being played,
    display it on my Slack status. Otherwise do nothing.

    """
    track = get_track_info()
    if track:
        status = f":fast_parrot: {track['artist_name']} - {track['track_name']} :fast_parrot:"
        set_user_status(status)


if __name__ == '__main__':
    main()
