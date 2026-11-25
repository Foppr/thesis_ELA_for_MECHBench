import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for each dimension with higher variability
        np.random.seed(42)
        self.amplitudes = np.random.uniform(0.3, 2.5, dim)
        self.frequencies = np.random.uniform(0.5, 8.0, dim)
        self.decay_rates = np.random.uniform(0.05, 2.0, dim)
        self.saddle_weights = np.random.uniform(-1.5, 1.5, dim)
        self.interference_strengths = np.random.uniform(0.05, 1.2, dim)
        self.ridge_heights = np.random.uniform(0.05, 0.5, dim)
        self.chaotic_amplitudes = np.random.uniform(0.4, 0.8, dim)
        self.cross_coupling_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        
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
            
            # Exponentially decaying sinusoidal term with additional harmonic
            term1 = amp * np.exp(-decay * np.abs(xi)) * np.sin(freq * xi)
            term2 = 0.5 * amp * np.exp(-0.5 * decay * np.abs(xi)) * np.cos(2 * freq * xi)
            
            # Asymmetric saddle point contribution with cubic component
            saddle_contribution = self.saddle_weights[i] * (xi**2 + 0.3 * xi**3) * np.cos(xi)
            
            result += term1 + term2 + saddle_contribution
            
        # Add cross-dimensional interference with enhanced coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                interference = self.interference_strengths[i] * np.exp(-0.3 * (xi**2 + xj**2)) * np.sin(xi * xj)
                
                # Asymmetric interaction with dynamic weighting
                asymmetry = 1.0 + 0.5 * np.sin(0.7 * (i - j)) * np.cos(0.3 * (i + j))
                result += asymmetry * interference
                
        # Add cross-dimensional coupling with matrix-based weights
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += self.cross_coupling_strengths[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Add global scaling with dynamic adjustment
        global_scaling = 1.0 + 0.3 * np.sin(0.4 * self.dim) * np.cos(0.2 * self.dim)
        result *= global_scaling
        
        # Add chaotic modulation with higher frequency components
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = self.chaotic_amplitudes[i]
            chaotic_component += amp * np.exp(-0.15 * xi**2) * np.cos(6.0 * xi + 0.5 * i)
            
        result += 0.1 * chaotic_component
        
        # Add ridge-like structure with varying widths and heights
        ridge_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_height = self.ridge_heights[i]
            ridge_width = 0.5 + 0.3 * np.sin(0.4 * i)
            ridge_penalty += ridge_height * np.sin(xi / ridge_width)**2
            
        result += ridge_penalty
        
        # Add noise-like perturbations to increase complexity
        noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            noise += 0.02 * np.sin(10 * xi + i) * np.cos(5 * xi - i)
            
        result += noise
        
        # Add a global minimum perturbation to challenge convergence
        global_min_perturbation = 0.05 * np.sum(np.abs(x))
        result += global_min_perturbation
        
        # Add additional high-frequency chaotic components for increased complexity
        high_freq_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            high_freq_component += 0.2 * np.sin(15 * xi + i) * np.cos(8 * xi - i)
            
        result += high_freq_component
        
        # Add a non-separable component to increase algorithmic bias
        non_sep_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                non_sep_term += (x[i] + x[j])**2 * np.sin(x[i] * x[j])
        result += 0.1 * non_sep_term
        
        return result