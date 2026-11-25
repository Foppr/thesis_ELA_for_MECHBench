import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for radial basis functions
        self.chaotic_params = 2.5 + 1.5 * np.sin(np.arange(dim) * 0.7)
        # Asymmetric saddle point locations
        self.saddle_points = np.array([np.sin(i * 0.8) * (i % 3 == 0) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic modulation
        rbf = 0.0
        for i in range(self.dim):
            # Chaotic scaling of RBF centers and widths
            center = self.chaotic_params[i] * np.cos(x[i] * 0.5)
            width = 1.2 + 0.8 * np.sin(i * 0.6)
            rbf += np.exp(-width * (x[i] - center)**2) * np.sin(x[i] * 2.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_osc = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.0 * np.cos(i * 0.4) * (i % 2 == 0)
            amp = 0.8 + 0.4 * np.sin(i * 0.7)
            sin_osc += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Asymmetric saddle point term
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i] - self.saddle_points[i])**2 * \
                          (1.0 + 0.3 * np.sin(x[i] * 1.5)) * \
                          np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling = 0.5 + 0.5 * np.sin(i * 0.3) * self.chaotic_params[i]
            cross_term += coupling * x[i] * np.sin(x[j] * 1.2) * np.cos(x[i] * 0.8)
        
        # Final multimodal landscape with adjusted weights
        result = 0.4 * np.sum(x**2) + 0.3 * rbf + 0.2 * sin_osc + \
                 0.05 * saddle_term + 0.05 * cross_term
        
        return result