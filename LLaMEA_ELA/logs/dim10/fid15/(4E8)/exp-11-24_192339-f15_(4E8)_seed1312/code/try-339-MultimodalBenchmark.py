import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired superposition weights
        self.weights = np.random.uniform(0.8, 2.5, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Time-varying chaotic parameters
        self.chaos_params = np.random.uniform(0.1, 0.9, dim)
        # Ridge structure parameters
        self.ridge_params = np.random.uniform(0.5, 2.0, dim)
        # Fractal scaling factors
        self.fractal_scales = np.random.uniform(0.3, 0.8, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired superposition term with enhanced interference
        quantum_term = 0
        for i in range(self.dim):
            # Enhanced superposition with multiple phase components
            superposition = (np.sin(self.weights[i] * x[i] + self.phases[i]) * 
                           np.cos(self.weights[i] * x[i] + self.phases[i] + np.pi/4) +
                           0.5 * np.sin(2 * self.weights[i] * x[i] + self.phases[i] + np.pi/6))
            quantum_term += superposition * np.exp(-0.1 * x[i]**2)
        
        # Enhanced time-varying chaotic attractor with dynamic coupling
        chaotic_term = 0
        for i in range(self.dim):
            # Dynamic coupling with next and previous dimensions (circular)
            j = (i + 1) % self.dim
            k = (i - 1) % self.dim
            # Enhanced chaotic modulation with multi-scale coupling
            chaotic_mod = (self.chaos_params[i] * np.sin(x[i] + x[j]) * 
                          np.cos(0.5 * x[i] + 0.3 * x[k]))
            chaotic_term += chaotic_mod * np.exp(-0.05 * (x[i]**2 + x[j]**2 + x[k]**2))
        
        # Adaptive ridge structure with variable steepness and fractal scaling
        ridge_term = 0
        for i in range(self.dim):
            # Ridge with exponential scaling, adaptive steepness, and fractal modulation
            ridge = (self.ridge_params[i] * np.exp(-0.5 * (x[i] - 1.0)**2) * 
                    (np.sin(3.0 * x[i]) + np.cos(2.0 * x[i])) *
                    (1.0 + self.fractal_scales[i] * np.sin(7.0 * x[i])))
            ridge_term += ridge
        
        # Enhanced non-separable high-order interaction with fractal-like behavior
        interaction_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # High-order polynomial interaction with chaotic modulation and fractal scaling
                poly_interaction = (x[i]**3 + x[j]**3) * np.sin(0.5 * (x[i] + x[j]))
                # Add enhanced fractal-like scaling factor
                scale_factor = 1.0 + 0.4 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[j])
                interaction_term += poly_interaction * scale_factor
        
        # Multi-scale oscillatory component with dynamic frequency and phase modulation
        oscillatory_term = 0
        for i in range(self.dim):
            # Multiple frequency components with time-varying modulation and phase coupling
            freq1 = 2.0 + 1.5 * np.sin(x[i] * 0.3 + self.phases[i])
            freq2 = 3.0 + 2.0 * np.cos(x[i] * 0.4 + self.phases[(i+1)%self.dim])
            oscillatory_term += (np.sin(freq1 * x[i]) + np.cos(freq2 * x[i])) * \
                              np.exp(-0.15 * x[i]**2)
        
        # Asymmetric multimodal with quantum-like interference and enhanced complexity
        asym_term = 0
        for i in range(self.dim):
            # Interference pattern with quantum-like phase differences and fractal modulation
            phase_diff = np.sin(x[i] * 0.5 + self.phases[i]) + np.cos(x[i] * 0.7 + self.phases[(i+2)%self.dim])
            asym_term += (np.sin(x[i] * (2.0 + phase_diff)) * 
                         np.cos(x[i] * (3.0 - phase_diff)) * 
                         np.exp(-0.2 * x[i]**2) *
                         (1.0 + 0.3 * np.sin(4.0 * x[i])))
        
        # Combine all components with dynamic weighting
        total = 0.35 * quantum_term + \
                0.25 * chaotic_term + \
                0.15 * ridge_term + \
                0.15 * interaction_term + \
                0.10 * oscillatory_term + \
                0.05 * asym_term
        
        # Add global scaling and enhanced noise to increase complexity
        return total * (1.0 + 0.25 * np.sin(np.sum(x) * 0.1)) + 0.02 * np.random.rand()