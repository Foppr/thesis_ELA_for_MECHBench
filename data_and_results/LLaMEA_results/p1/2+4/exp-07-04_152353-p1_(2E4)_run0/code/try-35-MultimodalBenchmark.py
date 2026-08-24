import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Polynomial terms with varying degrees to create flat and steep regions
        f1 = np.sum(x_normalized**4 + 0.5 * x_normalized**2)
        
        # Trigonometric components with multiple frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized) + 
                    np.sin(7 * np.pi * x_normalized) * np.cos(5 * np.pi * x_normalized))
        
        # Radial basis function components with different centers and widths
        centers = np.linspace(-1, 1, min(5, self.dim))
        rbfs = 0
        for i in range(min(5, self.dim)):
            center = centers[i] if self.dim > 1 else 0
            rbfs += np.exp(-5 * (x_normalized - center)**2)
        f3 = rbfs
        
        # Asymmetric coupling between dimensions with varying strength
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling += (x_normalized[i] * x_normalized[j] + 
                           0.3 * x_normalized[i]**3 * x_normalized[j]**2)
        
        # Add a global structure with periodic modulation and noise
        periodic = np.sum(np.sin(4 * np.pi * x_normalized) + 
                         np.cos(6 * np.pi * x_normalized))
        
        # Combine all components with adaptive weights
        result = 0.25 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * coupling + 0.1 * periodic
        
        # Add a saddle point structure with negative curvature
        saddle = np.sum(x_normalized**6 - 3 * x_normalized**4 + 2 * x_normalized**2)
        result += 0.05 * saddle
        
        return result