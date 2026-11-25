import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Chaotic multimodal component with logarithmic sine modulations
        multimodal = 0
        for i in range(self.dim):
            # Logarithmic frequency modulation
            freq = 3.0 * np.log(i + 2) / np.log(self.dim + 1)
            # Sine-based multimodal term with dynamic amplitude
            amplitude = 1.0 + 0.5 * np.sin(0.5 * i * np.pi)
            multimodal += amplitude * np.sin(freq * x[i])**4 + 0.3 * np.exp(-0.2 * (x[i] / 1.5)**2) * np.cos(freq * x[i])**6
        
        # Radial basis function component with adaptive bandwidth
        rbf = 0
        for i in range(self.dim):
            # Adaptive bandwidth based on dimensionality
            bandwidth = 1.0 + 0.2 * np.log(i + 1)
            rbf += np.exp(-0.5 * (x[i] / bandwidth)**2)
        
        # Dynamic polynomial coupling with varying exponents
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic exponents based on indices
                exp_i = 2 + 0.5 * (i % 3)
                exp_j = 3 + 0.3 * (j % 4)
                polynomial += 0.05 * (x[i] ** exp_i) * (x[j] ** exp_j)
        
        # Adaptive scaling factor
        scale_factor = 1.2 + 0.1 * np.sin(0.3 * self.dim)
        
        # Dynamic shift component
        shift = 0.5 * np.sum(np.abs(x)) * (1.0 + 0.2 * np.sin(0.4 * np.sum(x)))
        
        # Combined function with chaotic characteristics
        return sphere + scale_factor * (0.2 * multimodal + 0.1 * rbf + 0.03 * polynomial) + shift