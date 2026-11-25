import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(20 * np.pi * x_norm)**2 + np.sin(10 * np.pi * x_norm)**2)
        
        # Product term creating complex landscape with multiple peaks
        f3 = np.prod(np.cos(1.2 * np.pi * x_norm) + 0.5)
        
        # Higher-order polynomial interaction terms
        f4 = np.sum(x_norm**6 + 0.7 * x_norm**5 + 0.3 * x_norm**4)
        
        # Shifted global minimum term with non-linear transformation
        f5 = np.sum((x_norm + 0.2)**6)
        
        # Additional cross-term interaction creating intricate landscape
        f6 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Chaotic logistic map component for enhanced complexity
        logistic_seq = np.array([0.5])
        for i in range(self.dim - 1):
            logistic_seq = np.append(logistic_seq, 4 * logistic_seq[i] * (1 - logistic_seq[i]))
        f7 = np.sum(logistic_seq * x_norm**3)
        
        # Combine all terms with varying weights
        return 0.1 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.1 * f5 + 0.1 * f6 + 0.1 * f7 + 3.0