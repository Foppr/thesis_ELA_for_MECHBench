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
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired superposition term
        quantum_term = 0
        for i in range(self.dim):
            # Superposition of sine and cosine with phase modulation
            superposition = np.sin(self.weights[i] * x[i] + self.phases[i]) * \
                           np.cos(self.weights[i] * x[i] + self.phases[i] + np.pi/4)
            quantum_term += superposition * np.exp(-0.1 * x[i]**2)
        
        # Time-varying chaotic attractor with dynamic coupling
        chaotic_term = 0
        for i in range(self.dim):
            # Dynamic coupling with next dimension (circular)
            j = (i + 1) % self.dim
            # Chaotic modulation with time-varying parameter
            chaotic_mod = self.chaos_params[i] * np.sin(x[i] + x[j])
            chaotic_term += chaotic_mod * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Adaptive ridge structure with variable steepness
        ridge_term = 0
        for i in range(self.dim):
            # Ridge with exponential scaling and adaptive steepness
            ridge = self.ridge_params[i] * np.exp(-0.5 * (x[i] - 1.0)**2) * \
                   np.sin(3.0 * x[i]) + np.cos(2.0 * x[i])
            ridge_term += ridge
        
        # Non-separable high-order interaction with fractal-like behavior
        interaction_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # High-order polynomial interaction with chaotic modulation
                poly_interaction = (x[i]**3 + x[j]**3) * np.sin(0.5 * (x[i] + x[j]))
                # Add fractal-like scaling factor
                scale_factor = 1.0 + 0.3 * np.sin(5.0 * x[i])
                interaction_term += poly_interaction * scale_factor
        
        # Multi-scale oscillatory component with dynamic frequency
        oscillatory_term = 0
        for i in range(self.dim):
            # Multiple frequency components with time-varying modulation
            freq1 = 2.0 + 1.5 * np.sin(x[i] * 0.3)
            freq2 = 3.0 + 2.0 * np.cos(x[i] * 0.4)
            oscillatory_term += (np.sin(freq1 * x[i]) + np.cos(freq2 * x[i])) * \
                              np.exp(-0.15 * x[i]**2)
        
        # Asymmetric multimodal with quantum-like interference
        asym_term = 0
        for i in range(self.dim):
            # Interference pattern with quantum-like phase differences
            phase_diff = np.sin(x[i] * 0.5) + np.cos(x[i] * 0.7)
            asym_term += np.sin(x[i] * (2.0 + phase_diff)) * \
                        np.cos(x[i] * (3.0 - phase_diff)) * \
                        np.exp(-0.2 * x[i]**2)
        
        # Combine all components with dynamic weighting
        total = 0.35 * quantum_term + \
                0.25 * chaotic_term + \
                0.15 * ridge_term + \
                0.15 * interaction_term + \
                0.10 * oscillatory_term + \
                0.05 * asym_term
        
        # Add global scaling and noise to increase complexity
        return total * (1.0 + 0.2 * np.sin(np.sum(x) * 0.1)) + 0.01 * np.random.rand()