import numpy as np

class AdaptiveRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.amplitudes = np.random.uniform(1.5, 3.5, dim)
        self.frequencies = np.random.uniform(2.0, 6.0, dim)
        self.decay_rates = np.random.uniform(0.2, 1.5, dim)
        self.saddle_positions = np.random.uniform(-3.5, 3.5, dim)
        self.noise_amplitudes = np.random.uniform(0.1, 0.4, dim)
        self.fractal_exponents = np.random.uniform(0.2, 0.7, dim)
        self.ridge_strengths = np.random.uniform(0.5, 2.0, dim)
        
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
            
            # Exponentially decaying sinusoidal term with enhanced nonlinearity
            term = amp * np.exp(-decay * np.abs(xi)) * np.sin(freq * xi + 0.5 * np.sin(3.0 * xi))
            result += term
            
        # Add saddle-node bifurcation points with ridge attraction
        for i in range(self.dim):
            xi = x[i]
            saddle_pos = self.saddle_positions[i]
            ridge_strength = self.ridge_strengths[i]
            
            # Saddle point with ridge attraction and enhanced cubic terms
            saddle_term = (xi - saddle_pos)**2 * np.exp(-0.5 * (xi - saddle_pos)**2) + \
                         0.15 * (xi - saddle_pos)**3 + \
                         ridge_strength * np.sin(2.0 * (xi - saddle_pos))**2
            result += saddle_term
            
        # Add cross-dimensional fractal coupling with scale invariance
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Fractal coupling with power-law scaling and additional sinusoidal modulation
                coupling_strength = 0.6 * np.abs(xi - xj)**self.fractal_exponents[i]
                cross_term = coupling_strength * np.cos(2.0 * (xi + xj)) * np.exp(-0.1 * np.abs(xi - xj))
                result += cross_term
                
        # Add scale-invariant fractal noise with enhanced chaotic components
        for i in range(self.dim):
            xi = x[i]
            noise_amp = self.noise_amplitudes[i]
            fractal_exp = self.fractal_exponents[i]
            
            # Fractal noise with power-law scaling and chaotic modulation
            noise = noise_amp * np.sin(12.0 * xi + 0.3 * i) * np.cos(7.0 * xi)
            noise *= np.abs(xi)**fractal_exp
            noise += 0.05 * np.sin(25.0 * xi) * np.cos(15.0 * xi)
            result += noise
            
        # Add global scaling and non-linear transformation with enhanced ridge effects
        global_factor = 1.0 + 0.3 * np.sin(np.sum(x) / self.dim) * np.cos(0.5 * np.sum(x))
        result *= global_factor
        
        # Add adaptive coupling term that changes based on dimensionality
        if self.dim > 2:
            coupling_term = 0.0
            for i in range(self.dim):
                coupling_term += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 1))
            result += 0.2 * coupling_term * np.exp(-0.05 * self.dim)
            
        return result