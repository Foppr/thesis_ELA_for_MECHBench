import numpy as np

class ChaoticSineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic frequency modulation for sine components
        self.freq_mod = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.78 + np.pi/4)
        # Radial basis function centers with chaotic positioning
        self.rbf_centers = -3.0 + 6.0 * np.random.rand(dim, dim)
        # Asymmetric gradient weights
        self.gradient_weights = 1.0 + 0.5 * np.sin(np.arange(dim) * 0.92)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with varying frequencies
        sine_component = 0.0
        for i in range(self.dim):
            freq = self.freq_mod[i] * (1.0 + 0.3 * np.sin(x[i]))
            sine_component += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * \
                             np.exp(-0.1 * np.abs(x[i]))
        
        # Radial basis function component with chaotic centers
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                dist = np.sum((x - self.rbf_centers[i, :]) ** 2)
                rbf_sum += np.exp(-0.5 * dist) * np.sin(x[j])
            rbf_component += rbf_sum
        
        # Asymmetric gradient field with chaotic modulation
        grad_field = 0.0
        for i in range(self.dim):
            grad_term = self.gradient_weights[i] * (x[i]**3 - 3*x[i]) * \
                       np.exp(-0.2 * x[i]**2)
            grad_field += grad_term
        
        # Cross-dimensional coupling with asymmetric weights
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            weight = 0.8 + 0.4 * np.sin(i * 0.6) * np.cos(x[i])
            coupling += weight * np.sin(2.5 * x[i]) * np.cos(1.8 * x[j]) * \
                       (1.0 + 0.2 * np.sin(x[i] + x[j]))
        
        # Combined objective with adaptive weights
        result = 0.3 * np.sum(x**2) + 0.4 * sine_component + 0.2 * rbf_component + \
                 0.15 * grad_field + 0.1 * coupling
        
        return result