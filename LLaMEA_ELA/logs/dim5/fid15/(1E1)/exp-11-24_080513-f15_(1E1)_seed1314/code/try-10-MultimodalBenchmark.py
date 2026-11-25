import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic_term = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal perturbations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (1.5 * np.sin(7 * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.2)**2) + 
                        2.0 * np.sin(13 * np.pi * x_normalized[i]) * np.exp(-0.3 * (x_normalized[i] + 0.3)**2) + 
                        1.2 * np.sin(17 * np.pi * x_normalized[i]) * np.exp(-0.2 * (x_normalized[i] - 0.5)**2))
        
        # Add a polynomial term to increase complexity with mixed exponents and higher-order terms
        poly_term = 0.0
        for i in range(self.dim):
            if i % 4 == 0:
                poly_term += x_normalized[i]**9
            elif i % 4 == 1:
                poly_term += x_normalized[i]**6
            elif i % 4 == 2:
                poly_term += x_normalized[i]**8
            else:
                poly_term += x_normalized[i]**5
        
        # Add interaction terms between dimensions to increase problem complexity with higher-order coupling
        interaction_term = 0.0
        for i in range(self.dim-1):
            interaction_term += (x_normalized[i] - x_normalized[i+1])**4 * np.exp(-0.2 * (x_normalized[i] + x_normalized[i+1])**2) + \
                               (x_normalized[i] + x_normalized[i+1])**5 * np.exp(-0.15 * (x_normalized[i] - x_normalized[i+1])**2) + \
                               (x_normalized[i] * x_normalized[i+1])**3 * np.exp(-0.1 * (x_normalized[i]**2 + x_normalized[i+1]**2))
        
        # Add a Gaussian hill term to create additional local optima with varying heights
        gaussian_hill = 0.0
        for i in range(self.dim):
            gaussian_hill += 0.7 * np.exp(-3.0 * (x_normalized[i] - 0.1)**2) * np.sin(5 * np.pi * x_normalized[i]) + \
                            0.4 * np.exp(-2.5 * (x_normalized[i] + 0.2)**2) * np.cos(6 * np.pi * x_normalized[i])
        
        # Add a novel cross-dimensional oscillatory component with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(3 * np.pi * (x_normalized[i] + x_normalized[j])) * np.exp(-0.3 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Combine all terms with adjusted weights to create a highly multimodal landscape
        return quadratic_term + 0.3 * sin_term + 0.05 * poly_term + 0.15 * interaction_term + 0.15 * gaussian_hill + 0.08 * cross_term + 0.03 * np.sum(np.sin(9 * np.pi * x_normalized) * np.exp(-0.2 * x_normalized**2))