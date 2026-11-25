import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for sinusoidal components
        self.freq_params = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        # Precompute radial basis centers and widths
        self.centers = np.random.uniform(-3.0, 3.0, dim)
        self.widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = 1.0 + 0.3 * np.sin(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(0.5 * x[i])
            
        # Add radial basis function component with random centers and widths
        for i in range(self.dim):
            result += np.exp(-0.5 * ((x[i] - self.centers[i]) / self.widths[i])**2)
            
        # Add cross-dimensional coupling terms with varying interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for efficiency
                strength = 0.1 * (1 + np.sin(i * 0.3) * np.cos(j * 0.4))
                result += strength * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Add a modified Ackley-like function component for enhanced multimodality
        sum_sq = np.sum(x**2)
        sum_cos = np.sum(np.cos(2 * np.pi * x))
        result += -20 * np.exp(-0.2 * np.sqrt(sum_sq / self.dim)) - np.exp(sum_cos / self.dim) + 20 + np.e
        
        # Add a periodic component with varying frequencies and phases
        for i in range(self.dim):
            phase = i * 0.3
            result += 0.5 * np.sin(3 * x[i] + phase) * np.cos(2 * x[i] - phase)
            
        # Add conditioning through polynomial scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**4 + 0.1 * x[i]**3 + 0.01 * x[i]**2) * np.cos(0.5 * x[i])
        result += 0.01 * poly_term
        
        # Add global scaling with sinusoidal modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.2 * dist_from_origin) * np.cos(0.4 * dist_from_origin))
        
        return result