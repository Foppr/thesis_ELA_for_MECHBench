import numpy as np

class ExponentialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with radial basis functions
        exp_component = 0
        for i in range(self.dim):
            # Radial distance from origin
            r = np.sqrt(np.sum(x**2))
            # Exponential decay with dimension-dependent rate
            decay_rate = 0.5 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            exp_component += np.exp(-decay_rate * r) * np.cos(i * np.pi / (self.dim + 2) * x[i])
        
        # Sine-wave modulated radial basis functions
        sine_rbf_component = 0
        for i in range(self.dim):
            # Modulation frequency based on dimension
            freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 3))
            # Radial distance with sine modulation
            r = np.sqrt(np.sum(x**2)) * (1.0 + 0.2 * np.sin(freq * x[i]))
            # Sine-wave modulated RBF
            sine_rbf_component += np.sin(r) * np.exp(-0.5 * (x[i] / (1.0 + i * 0.1))**2)
        
        # Dynamic penalty terms with adaptive thresholds
        penalty_component = 0
        for i in range(self.dim):
            # Adaptive threshold based on dimension and position
            threshold = 3.0 + 1.5 * np.sin(i * np.pi / (self.dim + 4)) + 0.5 * np.cos(x[i])
            if abs(x[i]) > threshold:
                penalty_component += (abs(x[i]) - threshold)**2 * (1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 2)))
            else:
                penalty_component += -np.exp(-0.5 * (x[i] / (1.0 + i * 0.1))**2) * (1.0 + 0.2 * np.cos(i * np.pi / (self.dim + 5)))
        
        # Cross-term interaction with dynamic coupling coefficients
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength
                coupling = 0.6 + 0.4 * np.sin((i + j) * np.pi / (self.dim + 2))
                # Cross interaction with sine modulation
                cross_term += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Global scaling and normalization
        norm_factor = 1.0 + 0.2 * np.cos(self.dim * np.pi / 8)
        
        # Combine all components with dimension-dependent weights
        weight1 = 0.35 + 0.1 * np.sin(self.dim * np.pi / 4)
        weight2 = 0.30 + 0.15 * np.cos(self.dim * np.pi / 5)
        weight3 = 0.20 + 0.1 * np.sin(self.dim * np.pi / 6)
        weight4 = 0.15 + 0.1 * np.cos(self.dim * np.pi / 7)
        
        return weight1 * exp_component + weight2 * sine_rbf_component + weight3 * penalty_component + weight4 * cross_term * norm_factor