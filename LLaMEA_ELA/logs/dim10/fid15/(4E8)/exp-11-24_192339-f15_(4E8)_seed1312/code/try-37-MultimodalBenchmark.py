import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial base term with mixed degrees
        poly_term = np.sum(x_normalized**4 + 0.5 * x_normalized**3 + 0.2 * x_normalized**2)
        
        # Trigonometric components with varying frequencies and phases
        trig_term1 = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        trig_term2 = np.sum(np.sin(5 * np.pi * x_normalized) * np.sin(4 * np.pi * x_normalized))
        
        # Radial basis function components with different centers and widths
        centers = np.linspace(-1, 1, min(5, self.dim))
        rbfs = []
        for i in range(min(5, self.dim)):
            center = centers[i]
            width = 0.5 + 0.5 * (i / max(1, self.dim - 1))
            rbf = np.exp(-width * (x_normalized - center)**2)
            rbfs.append(rbf)
        rbf_term = np.sum(np.array(rbfs))
        
        # Cross-terms creating interaction between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(2 * np.pi * (x_normalized[i] - x_normalized[j]))
        
        # Exponential decay with dimension-dependent scaling
        exp_decay = np.sum(np.exp(-0.5 * x_normalized**2) * (1 + 0.1 * np.abs(x_normalized)))
        
        # Combine all terms with appropriate weights
        return poly_term + 0.3 * trig_term1 + 0.2 * trig_term2 + 0.1 * rbf_term + 0.05 * cross_term + 0.1 * exp_decay