import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for sinusoidal components
        self.freq_params = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        # Precompute radial basis centers and widths
        self.rbf_centers = np.random.uniform(-3.0, 3.0, dim)
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = 1.0 + 0.3 * np.sin(i * 0.8)
            result += amp * np.sin(freq * x[i]) * np.cos(2 * freq * x[i])
            
        # Add radial basis function components
        for i in range(self.dim):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            result += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Add cross-dimensional coupling with sine and cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                result += 0.1 * coupling
                
        # Add a modified Schwefel-like component with variable scaling
        schwefel_sum = 0.0
        for i in range(self.dim):
            schwefel_sum += -x[i] * np.sin(np.sqrt(np.abs(x[i])))
        result += 0.05 * schwefel_sum
        
        # Add a chaotic logistic map component with dynamic parameter
        chaos_param = 3.9 + 0.1 * np.sin(np.sum(x) * 0.1)
        for i in range(self.dim):
            result += 0.02 * chaos_param * x[i] * (1 - x[i]**2)
            
        # Add a polynomial term with high-order exponents to increase conditioning
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += 0.01 * x[i]**8 + 0.005 * x[i]**6
        result += poly_term
        
        # Add a global scaling factor with multiple harmonic components
        dist_from_origin = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(0.3 * dist_from_origin)
        result *= scaling
        
        return result