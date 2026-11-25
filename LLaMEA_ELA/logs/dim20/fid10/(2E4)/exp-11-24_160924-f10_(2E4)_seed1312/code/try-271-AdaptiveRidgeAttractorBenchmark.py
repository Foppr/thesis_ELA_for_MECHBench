import numpy as np

class AdaptiveRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.amplitudes = np.random.uniform(1.5, 4.0, dim)
        self.frequencies = np.random.uniform(2.0, 8.0, dim)
        self.decay_rates = np.random.uniform(0.2, 1.5, dim)
        self.saddle_positions = np.random.uniform(-3.5, 3.5, dim)
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, dim)
        self.fractal_exponents = np.random.uniform(0.2, 0.9, dim)
        self.ridge_heights = np.random.uniform(0.5, 2.0, dim)
        self.attractor_strengths = np.random.uniform(0.3, 1.2, dim)
        
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
            
        # Add chaotic saddle points with ridge attractors
        for i in range(self.dim):
            xi = x[i]
            saddle_pos = self.saddle_positions[i]
            ridge_height = self.ridge_heights[i]
            
            # Saddle point with quadratic and cubic terms plus ridge attraction
            saddle_term = (xi - saddle_pos)**2 * np.exp(-0.5 * (xi - saddle_pos)**2) + \
                         0.1 * (xi - saddle_pos)**3 + \
                         ridge_height * np.exp(-0.1 * (xi - saddle_pos)**2)
            result += saddle_term
            
        # Add cross-dimensional fractal coupling with adaptive coupling strength
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Adaptive coupling with power-law scaling and dynamic strength
                coupling_strength = 0.3 * np.abs(xi - xj)**self.fractal_exponents[i] * \
                                  (1.0 + 0.5 * np.sin(0.5 * (xi + xj)))
                cross_term = coupling_strength * np.cos(3.0 * (xi + xj))
                result += cross_term
                
        # Add scale-invariant fractal noise with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            noise_amp = self.noise_amplitudes[i]
            fractal_exp = self.fractal_exponents[i]
            
            # Fractal noise with chaotic modulation and power-law scaling
            chaotic_mod = 1.0 + 0.3 * np.sin(15.0 * xi) * np.cos(7.0 * xi)
            noise = noise_amp * np.sin(12.0 * xi + 0.5 * i) * np.cos(6.0 * xi) * chaotic_mod
            noise *= np.abs(xi)**fractal_exp
            result += noise
            
        # Add adaptive attractor terms that change based on global position
        global_pos = np.sum(x) / self.dim
        for i in range(self.dim):
            xi = x[i]
            attractor_strength = self.attractor_strengths[i] * (1.0 + 0.2 * np.sin(2.0 * global_pos))
            attractor_term = attractor_strength * (xi - global_pos)**2
            result += attractor_term
            
        # Add non-linear transformation for increased complexity
        result = result * (1.0 + 0.1 * np.sin(0.5 * np.sum(x**2)))
        
        return result