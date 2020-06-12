package hello.storage;

public class StorageFileNoutFoundException extends StorageException {

    public StorageFileNoutFoundException(String message) {
        super(message);
    }

    public StorageFileNoutFoundException(String message, Throwable cause) {
        super(message, cause);
    }
}
