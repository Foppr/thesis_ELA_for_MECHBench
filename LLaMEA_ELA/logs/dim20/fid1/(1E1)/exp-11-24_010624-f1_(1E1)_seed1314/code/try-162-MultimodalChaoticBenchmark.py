import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for sinusoidal components
        self.freq_params = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        # Precompute radial basis centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, dim)
        self.widths = 0.5 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = 1.0 + 0.3 * np.sin(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Add radial basis function component
        for i in range(self.dim):
            result += np.exp(-0.5 * ((x[i] - self.centers[i]) / self.widths[i])**2)
            
        # Add cross-dimensional coupling with exponentially decaying strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling = np.exp(-0.1 * dist) * np.sin(x[i] * x[j])
                result += 0.5 * coupling
                
        # Add polynomial terms with varying exponents and coefficients
        for i in range(self.dim):
            exp_val = 2 + 2 * np.sin(i * 0.3)
            coeff = 0.5 + 0.5 * np.cos(i * 0.4)
            result += coeff * x[i]**exp_val
            
        # Add a global scaling component with multiple harmonic frequencies
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.3 * np.sin(0.2 * dist_from_origin) * np.cos(0.5 * dist_from_origin) * np.sin(0.8 * dist_from_origin))
        
        # Add noise component
        noise = 0.01 * np.sum(np.sin(x * 7))
        result += noise
        
        # Add a modified Ackley-like term for enhanced multimodality
        sum_sq = np.sum(x**2)
        sum_cos = np.sum(np.cos(2 * np.pi * x))
        ackley_term = -20 * np.exp(-0.2 * np.sqrt(sum_sq/self.dim)) - np.exp(sum_cos/self.dim) + 20 + np.exp(1)
        result += 0.1 * ackley_term
        
        # Add a modified Griewank function component
        griewank_term = np.sum(x**2/4000) - np.prod(np.cos(x/np.sqrt(np.arange(1, self.dim+1)))) + 1
        result += 0.05 * griewank_term
        
        return result