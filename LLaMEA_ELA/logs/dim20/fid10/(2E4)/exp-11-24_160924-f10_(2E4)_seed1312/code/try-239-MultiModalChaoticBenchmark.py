import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for each dimension with increased complexity
        np.random.seed(42)
        self.amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.frequencies = np.random.uniform(1.0, 15.0, dim)
        self.decay_rates = np.random.uniform(0.1, 3.0, dim)
        self.saddle_weights = np.random.uniform(-2.0, 2.0, dim)
        self.interference_strengths = np.random.uniform(0.1, 2.0, dim)
        self.ridge_heights = np.random.uniform(0.15, 0.5, dim)
        self.ridge_widths = np.random.uniform(0.6, 2.0, dim)
        self.noise_amplitudes = np.random.uniform(0.03, 0.15, dim)
        self.chaotic_amplitudes = np.random.uniform(0.4, 1.0, dim)
        self.oscillation_frequencies = np.random.uniform(15.0, 25.0, dim)
        self.fractal_scales = np.random.uniform(0.3, 0.8, dim)
        self.gradient_modulation = np.random.uniform(0.5, 1.5, dim)
        
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
            
            # Exponentially decaying sinusoidal term with modified phase and enhanced modulation
            term1 = amp * np.exp(-decay * np.abs(xi)) * np.sin(freq * xi + 0.5 * i)
            
            # Enhanced asymmetric saddle point contribution with variable dominance and nonlinearity
            saddle_contribution = self.saddle_weights[i] * xi**3 * np.cos(0.7 * xi + 0.3 * i) + 0.2 * xi**2
            
            result += term1 + saddle_contribution
            
        # Add cross-dimensional interference with enhanced asymmetry and coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                interference = self.interference_strengths[i] * np.exp(-0.5 * (xi**2 + xj**2)) * np.sin(xi * xj + 0.2 * (i - j))
                
                # Enhanced asymmetric interaction based on dimension indices with dynamic coupling
                asymmetry = 1.0 + 0.6 * np.sin(0.8 * (i - j) + 0.15 * i) * np.cos(0.3 * (i + j))
                result += asymmetry * interference
                
        # Add global scaling with modified harmonic components and additional complexity
        global_scaling = 1.0 + 0.2 * np.sin(0.3 * self.dim + 0.4 * np.sum(x)) * np.cos(0.1 * np.sum(x**2))
        result *= global_scaling
        
        # Add enhanced chaotic modulation with dynamic amplitudes and additional nonlinearities
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = self.chaotic_amplitudes[i] + 0.3 * np.sin(0.9 * i + 0.15 * np.sum(x)) * np.cos(0.2 * i)
            chaotic_component += amp * np.exp(-0.15 * xi**2) * np.cos(4.0 * xi + 0.25 * i)
            
        result += 0.1 * chaotic_component
        
        # Add refined ridge-like structure with variable heights, widths and additional nonlinear components
        ridge_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_height = self.ridge_heights[i] + 0.05 * np.sin(0.6 * i + 0.25 * np.sum(x))
            ridge_width = self.ridge_widths[i] + 0.3 * np.cos(0.4 * i)
            # Mutated: Changed from sin^3 to sin^4 for sharper ridges
            ridge_penalty += ridge_height * np.sin(ridge_width * xi)**4
            
        result += ridge_penalty
        
        # Add noise-like perturbations with increased complexity and dynamic modulation
        noise_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            noise_term += self.noise_amplitudes[i] * np.sin(8.0 * xi + 0.15 * i) * np.cos(4.0 * xi + 0.08 * np.sum(x)) * np.exp(-0.05 * xi**2)
            
        result += noise_term
        
        # Add additional high-frequency oscillatory components for increased complexity
        high_freq_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            high_freq_component += 0.12 * np.sin(self.oscillation_frequencies[i] * xi + 0.2 * i) * np.cos(10.0 * xi + 0.1 * np.sum(x))
            
        result += high_freq_component
        
        # Add fractal-like self-similarity components with recursive scaling and gradient modulation
        fractal_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Mutated: Changed fractal scale to be more aggressive
            scale_factor = self.fractal_scales[i] * (1.0 + 0.3 * np.sin(0.5 * i + 0.1 * np.sum(x)))
            fractal_component += scale_factor * np.sin(2.0 * xi) * np.cos(3.0 * xi)
            
        result += 0.05 * fractal_component
        
        # Add novel gradient modulation based on fractal characteristics
        gradient_modulation_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            mod_amp = self.gradient_modulation[i] + 0.1 * np.sin(0.3 * i + 0.05 * np.sum(x))
            gradient_modulation_term += mod_amp * np.cos(5.0 * xi) * np.sin(2.0 * xi)
            
        result += 0.08 * gradient_modulation_term
        
        return result