import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic dynamics and multi-scale interference
        self.alpha = 3.9
        self.beta = 0.5
        self.gamma = 0.3
        self.delta = 0.7
        self.epsilon = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with logistic map dynamics
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map component with chaotic modulation
            log_val = self.alpha * (x[i] / 5.0) * (1 - (x[i] / 5.0))
            chaotic += np.sin(log_val * 10.0) * np.cos(log_val * 5.0)
            
        # Multi-scale harmonic interference with fractal characteristics
        harmonic = 0.0
        for i in range(self.dim):
            # Multiple frequencies with varying amplitudes and phases
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            amps = [1.0, 0.8, 0.6, 0.4, 0.2]
            phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
            
            for f, a, p in zip(freqs, amps, phases):
                harmonic += a * np.sin(f * x[i] + p) * np.cos(f * x[i] / 2.0 + p)
                
        # Dynamic cross-dimensional coupling with adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Adaptive coupling based on distance and dimensionality
                dist_factor = 1.0 / (1.0 + np.exp(-self.gamma * abs(diff)))
                coupling += dist_factor * np.sin(2.0 * diff) * np.cos(3.0 * diff)
                
        # Fractal noise component with self-similar properties
        fractal = 0.0
        for i in range(self.dim):
            # Multiple fractal components at different scales
            scales = [1.0, 0.5, 0.25, 0.125]
            for s in scales:
                fractal += s * np.sin(x[i] / s) * np.cos(x[i] / (s * 2.0))
                
        # Dimensionality complexity with polynomial and exponential terms
        complexity = 0.0
        for i in range(self.dim):
            # Combination of polynomial and exponential terms with scaling factors
            complexity += (x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-self.delta * abs(x[i]))
            
        # Global modulation based on solution quality and proximity to optima
        modulation = 0.0
        norm_x = np.linalg.norm(x)
        if norm_x < 0.5:
            modulation = 10.0 * np.exp(-norm_x**2)
        elif norm_x > 4.5:
            modulation = 8.0 * np.exp(-(norm_x - 4.5)**2)
            
        # Add chaotic noise for enhanced ergodicity
        chaos_noise = 0.0
        for i in range(self.dim):
            chaos_noise += self.epsilon * np.sin(x[i] * 10.0) * np.cos(x[i] * 15.0)
            
        # Combine all components with adaptive weights
        result = 1.5 * chaotic + 1.2 * harmonic + 0.9 * coupling + 0.7 * fractal + 0.8 * complexity + modulation + chaos_noise
        
        # Add offset to ensure positive fitness and scale appropriately
        return result + 12.0 * self.dim