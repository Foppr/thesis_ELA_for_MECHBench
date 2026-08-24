import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial basis function component with adaptive width
        rbf = 0.0
        for i in range(self.dim):
            # Adaptive width based on dimension index
            width = 0.5 + 0.3 * np.sin(i * 0.5)
            rbf += np.exp(-0.5 * (x_normalized[i] / width)**2)
            
        # Polynomial cross-dimensional interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cubic interaction with varying strength
                strength = 0.3 + 0.2 * np.sin(i * 0.3 + j * 0.4)
                poly_interaction += strength * (x_normalized[i]**3 + x_normalized[j]**3) * (x_normalized[i] - x_normalized[j])**2
                
        # Multi-scale sinusoidal modulation
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(i * 0.7)
            amp = 1.5 + 0.8 * np.cos(i * 0.9)
            sinusoidal += amp * np.sin(freq * x_normalized[i]) * np.cos(2 * freq * x_normalized[i])
            
        # Asymmetric penalty with exponential decay
        penalty = 0.0
        for i in range(self.dim):
            # Asymmetric exponential penalty
            penalty += 2.0 * np.exp(-0.5 * (x_normalized[i] - 0.3)**2) - 0.5 * np.exp(-0.5 * (x_normalized[i] + 0.3)**2)
            
        # Central attraction with varying strength
        center_attraction = 0.0
        dist_from_center = np.sqrt(np.sum(x_normalized**2))
        center_attraction = 1.5 * (1.0 - np.exp(-0.3 * dist_from_center**2)) * np.sin(5 * dist_from_center)
        
        # Dimensional scaling with non-linear transformation
        scaling = 0.0
        for i in range(self.dim):
            # Apply a non-linear transformation to each dimension
            transformed = np.tanh(x_normalized[i] * (1.0 + 0.2 * np.sin(i * 0.8)))
            scaling += 0.8 * transformed**4
            
        # Cross-dimensional quadratic coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.2 * (x_normalized[i]**2 + x_normalized[j]**2) * np.sin(10 * (x_normalized[i] - x_normalized[j]))
                
        # Add a global minimum with a complex structure
        global_min = 0.0
        for i in range(self.dim):
            global_min += 0.1 * (x_normalized[i]**6 - 3 * x_normalized[i]**4 + 3 * x_normalized[i]**2 - 1)
            
        # Combine all components
        return rbf + poly_interaction + sinusoidal + penalty + center_attraction + scaling + coupling + global_min