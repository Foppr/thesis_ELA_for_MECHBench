import numpy as np

class ChaoticAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base chaotic component with nested sinusoids and increased complexity
        f = 0.0
        for i in range(self.dim):
            f += np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) * np.sin(7 * x_norm[i]) * np.cos(9 * x_norm[i])
            
        # Asymmetric saddle points with enhanced dynamic weights and non-linear bias
        for i in range(self.dim):
            # Asymmetric quadratic terms with directional bias and chaotic modulation
            bias = 0.5 * np.sin(i * 0.7) + 0.2 * np.cos(i * 1.3)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.3 * np.sinh(x[i]**2) + 0.1 * np.sin(11 * x[i])
            
        # Nested multi-scale modulations with increased coupling and fractal-like structure
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling
                modulation = np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[j]) * np.sin(5 * x_norm[i]) * np.cos(7 * x_norm[j])
                f += 0.3 * modulation * (1 + 0.1 * np.sin(i + j) + 0.05 * np.cos(i * j))
                
        # Dynamic gradient landscape based on proximity to critical points with enhanced sensitivity
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.5)) + 0.1 * np.abs(x[i] - np.cos(i * 0.3))
        scale_factor = 1.0 + 0.8 * np.exp(-proximity / 1.5)
        f *= scale_factor
        
        # Fractal-like complexity with recursive harmonic terms and increased dimensionality
        for i in range(self.dim):
            f += 0.15 * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i]) * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i])
            
        # Chaotic perturbations with higher frequency components and increased amplitude
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(23 * x_norm[i]) * np.cos(29 * x_norm[i]) * np.sin(31 * x_norm[i]) * np.cos(37 * x_norm[i])
        f += 0.1 * chaos
        
        # Strengthened global minimum attraction with higher-order polynomial terms
        f += 0.3 * np.sum(x**6) + 0.1 * np.sum(x**8)
        
        # Additional multi-modal structure with periodic peaks
        for i in range(self.dim):
            f += 0.2 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i])
            
        # Enhanced noise and irregularity with additional chaotic harmonic components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(41 * x_norm[i]) * np.cos(43 * x_norm[i]) + 0.03 * np.sin(47 * x_norm[i]) * np.cos(53 * x_norm[i])
        f += noise
        
        # Introduce irregular coupling between dimensions with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dynamic_weight = 0.2 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.1 * np.sin(i * j * 0.1)
                f += dynamic_weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add irregular fractal-like structures with recursive harmonic terms
        for i in range(self.dim):
            f += 0.05 * np.sin(29 * x_norm[i]) * np.cos(37 * x_norm[i]) * np.sin(41 * x_norm[i]) * np.cos(47 * x_norm[i]) * np.sin(53 * x_norm[i])
            
        # Introduce chaotic modulation with exponential decay and increased sensitivity
        exp_mod = 0.0
        for i in range(self.dim):
            exp_mod += np.exp(-0.5 * x[i]**2) * np.sin(61 * x_norm[i]) * np.cos(67 * x_norm[i])
        f += 0.15 * exp_mod
        
        # Add multi-scale periodicity with non-uniform frequencies and amplitudes
        periodicity = 0.0
        for i in range(self.dim):
            periodicity += 0.1 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i]) * np.cos(40 * x[i])
        f += periodicity
        
        # Enhanced chaotic sensitivity with higher-order coupling terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                for k in range(j+1, min(j+4, self.dim)):
                    coupling += 0.05 * np.sin(x[i] + x[j] + x[k]) * np.cos(x[i] - x[j] + x[k])
        f += coupling
        
        # Additional chaotic modulation with exponential decay and increased sensitivity
        exp_mod2 = 0.0
        for i in range(self.dim):
            exp_mod2 += np.exp(-0.3 * x[i]**2) * np.sin(71 * x_norm[i]) * np.cos(73 * x_norm[i]) * np.sin(79 * x_norm[i])
        f += 0.2 * exp_mod2
        
        # Introduce multi-scale fractal structure with recursive harmonic components
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.08 * np.sin(83 * x_norm[i]) * np.cos(89 * x_norm[i]) * np.sin(97 * x_norm[i]) * np.cos(101 * x_norm[i]) * np.sin(103 * x_norm[i]) * np.cos(107 * x_norm[i])
        f += fractal
        
        # Add enhanced asymmetric coupling with dynamic weights and irregular modulation
        asym_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                asym_weight = 0.15 * np.sin(i * 0.2) * np.cos(j * 0.6) + 0.08 * np.sin(i * j * 0.15)
                asym_coupling += asym_weight * np.sin(x[i] + x[j])**2 * np.cos(x[i] - x[j])**2
        f += asym_coupling
        
        # Introduce irregular multi-modal structure with higher-order polynomial terms
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.25 * np.sin(12 * x[i])**3 * np.cos(18 * x[i])**2 * np.sin(24 * x[i])**2
        f += multimodal
        
        return f