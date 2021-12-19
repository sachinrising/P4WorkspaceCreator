import WorkspaceCreator
import sys
import logging

if __name__ == "__main__":
    user, password, port, client, root, spec, placeholder = WorkspaceCreator.scan_args(
        sys.argv[1:])

    logger = logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(sys.stderr)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(name)s] [%(funcName)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    stream_handler.setFormatter(formatter)

    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

    if user == None or password == None or client == None or spec == None:
        logger.error(
            f"Unable to create workspace as invalid arguments passed: User: {user}, Client: {client}, Root: {root}, Spec File: {spec}, Placeholder: {placeholder}")

    WorkspaceCreator.intialize_and_create_workspace(user=user, password=password, port=port, client=client,
                                                    root=root, spec_file=spec, placeholder=placeholder, logger=logger)
