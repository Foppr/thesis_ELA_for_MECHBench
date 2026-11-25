import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for each dimension with golden ratio seeding
        np.random.seed(42)
        self.amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.frequencies = np.random.uniform(1.0, 8.0, dim)
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.saddle_weights = np.random.uniform(-1.5, 1.5, dim)
        self.interference_strengths = np.random.uniform(0.1, 1.0, dim)
        # Golden ratio based perturbations
        self.golden_ratio = (1 + np.sqrt(5)) / 2
        self.perturbation_seeds = [self.golden_ratio ** i for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add multi-modal sinusoidal components with exponential decay and golden ratio perturbations
        for i in range(self.dim):
            xi = x[i]
            amp = self.amplitudes[i]
            freq = self.frequencies[i]
            decay = self.decay_rates[i]
            
            # Exponentially decaying sinusoidal term with golden ratio modulation
            golden_mod = np.sin(self.perturbation_seeds[i] * xi)
            term1 = amp * np.exp(-decay * np.abs(xi)) * np.sin(freq * xi) * golden_mod
            
            # Asymmetric saddle point contribution with golden ratio influence
            saddle_contribution = self.saddle_weights[i] * xi**2 * np.cos(xi) * (1 + 0.2 * golden_mod)
            
            result += term1 + saddle_contribution
            
        # Add cross-dimensional interference with asymmetric coupling and golden ratio interactions
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                interference = self.interference_strengths[i] * np.exp(-0.5 * (xi**2 + xj**2)) * np.sin(xi * xj)
                
                # Asymmetric interaction based on dimension indices with golden ratio
                asymmetry = 1.0 + 0.4 * np.sin(0.5 * (i - j) + self.perturbation_seeds[i] * self.perturbation_seeds[j])
                result += asymmetry * interference
                
        # Add global scaling and multi-modal complexity with golden ratio influence
        global_scaling = 1.0 + 0.3 * np.sin(0.3 * self.dim + self.perturbation_seeds[0])
        result *= global_scaling
        
        # Add chaotic modulation with varying amplitudes based on golden ratio
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = 0.5 + 0.4 * np.sin(0.7 * i + self.perturbation_seeds[i])
            chaotic_component += amp * np.exp(-0.1 * xi**2) * np.cos(4.0 * xi)
            
        result += 0.1 * chaotic_component
        
        # Add ridge-like structure with varying heights and golden ratio perturbations
        ridge_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_height = 0.1 + 0.3 * np.sin(0.6 * i + self.perturbation_seeds[i])
            ridge_penalty += ridge_height * np.sin(2.0 * xi)**2
            
        result += ridge_penalty
        
        # Add hyper-chaotic component with multiple frequencies and golden ratio modulation
        hyper_chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq1 = 3.0 + 0.5 * np.sin(self.perturbation_seeds[i])
            freq2 = 7.0 + 0.3 * np.cos(self.perturbation_seeds[i])
            hyper_chaotic += (np.exp(-0.05 * xi**2) * np.sin(freq1 * xi) * np.cos(freq2 * xi))
            
        result += 0.08 * hyper_chaotic
        
        # Add multi-scale interference with different interaction patterns
        multi_scale = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                # Different interaction pattern with golden ratio influence
                scale_factor = 1.0 + 0.2 * np.sin(self.perturbation_seeds[i] * self.perturbation_seeds[j])
                multi_scale += scale_factor * np.exp(-0.3 * (xi**2 + xj**2)) * np.sin(3.0 * xi * xj)
                
        result += 0.15 * multi_scale
        
        return result