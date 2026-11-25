import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        self.decay_rates = np.random.uniform(0.1, 1.0, dim)
        self.saddle_positions = np.random.uniform(-4.0, 4.0, dim)
        self.noise_amplitudes = np.random.uniform(0.05, 0.3, dim)
        self.fractal_exponents = np.random.uniform(0.3, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add multi-modal sinusoidal components with exponential decay
        for i in range(self.dim):
            xi = x[i]
            amp = self.amplitudes[i]
            freq = self.frequencies[i]
            decay = self.decay_rates[i]
            
            # Exponentially decaying sinusoidal term
            term = amp * np.exp(-decay * np.abs(xi)) * np.sin(freq * xi)
            result += term
            
        # Add saddle-node bifurcation points
        for i in range(self.dim):
            xi = x[i]
            saddle_pos = self.saddle_positions[i]
            # Saddle point with quadratic and cubic terms
            saddle_term = (xi - saddle_pos)**2 * np.exp(-0.5 * (xi - saddle_pos)**2) + 0.1 * (xi - saddle_pos)**3
            result += saddle_term
            
        # Add cross-dimensional fractal coupling with scale invariance
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Fractal coupling with power-law scaling
                coupling_strength = 0.5 * np.abs(xi - xj)**self.fractal_exponents[i]
                cross_term = coupling_strength * np.cos(2.0 * (xi + xj))
                result += cross_term
                
        # Add scale-invariant fractal noise
        for i in range(self.dim):
            xi = x[i]
            noise_amp = self.noise_amplitudes[i]
            fractal_exp = self.fractal_exponents[i]
            
            # Fractal noise with power-law scaling
            noise = noise_amp * np.sin(10.0 * xi + 0.5 * i) * np.cos(5.0 * xi)
            noise *= np.abs(xi)**fractal_exp
            result += noise
            
        # Add global scaling and non-linear transformation
        global_factor = 1.0 + 0.2 * np.sin(np.sum(x) / self.dim)
        result *= global_factor
        
        return result