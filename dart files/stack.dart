class StackNode<T> {
  T data;

  StackNode<T>? below;

  StackNode(this.data);
}

class Stack<T> {
  StackNode<T>? top;

  int size;

  Stack()
      : top = null,
        size = 0;

  bool get isEmpty => top == null;

  T pop() {
    if (isEmpty) throw InvalidIndexError();
    var output = top!;
    top = top?.below;
    size--;

    return output.data;
  }

  T? peek() => top?.data;

  void push(T data) {
    var newNode = StackNode(data);
    if (isEmpty) {
      top = newNode;
    } else {
      newNode.below = top;
      top = newNode;
    }
    size++;
  }
}

class InvalidIndexError extends Error {
  @override
  String toString() => 'Invalid Index for this operation';
}

mixin BinaryHeapIndex {
  /// Parent index of [idx]
  int parentOf(int idx) =>
      idx >= 0 ? ((idx - 1) / 2).truncate() : throw InvalidIndexError();

  /// Left child index of [idx]
  int leftOf(int idx) => 2 * idx + 1;

  /// Right child index of [idx]
  int rightOf(int idx) => 2 * idx + 2;
}

/// Comparison logic of two objects, based on which nature of heaps will
/// be determined.
typedef Comparer<T> = bool Function(T parent, T child);

/// Base class for Heap
abstract class HeapBase<T> {
  /// Checks if this heap is empty
  bool get isEmpty;

  /// The length of this heap
  int get length;

  /// Inserts [item] into [this]
  void insert(T item);

  /// Inserts all [items] into [this]
  void insertMany(List<T> items);

  /// Heapifies all below [rootIndex]
  void heapify(int rootIndex);

  /// Pops from the heap
  T pop();

  /// Peeks the last item on heap
  T peek();
}
