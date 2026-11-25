import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic dynamics and multi-scale interference
        self.alpha = 3.8
        self.beta = 0.6
        self.gamma = 0.4
        self.delta = 0.8
        self.epsilon = 0.15
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with logistic map dynamics
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map component with chaotic modulation
            log_val = self.alpha * (x[i] / 5.0) * (1 - (x[i] / 5.0))
            chaotic += np.sin(log_val * 12.0) * np.cos(log_val * 7.0)
            
        # Multi-scale harmonic interference with fractal characteristics
        harmonic = 0.0
        for i in range(self.dim):
            # Multiple frequencies with varying amplitudes and phases
            freqs = [1.0, 2.5, 3.5, 4.5, 5.5]
            amps = [1.0, 0.7, 0.5, 0.3, 0.1]
            phases = [0.0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3]
            
            for f, a, p in zip(freqs, amps, phases):
                harmonic += a * np.sin(f * x[i] + p) * np.cos(f * x[i] / 3.0 + p)
                
        # Dynamic cross-dimensional coupling with adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Adaptive coupling based on distance and dimensionality
                dist_factor = 1.0 / (1.0 + np.exp(-self.gamma * abs(diff)))
                coupling += dist_factor * np.sin(3.0 * diff) * np.cos(4.0 * diff)
                
        # Fractal noise component with self-similar properties
        fractal = 0.0
        for i in range(self.dim):
            # Multiple fractal components at different scales
            scales = [1.0, 0.5, 0.25, 0.125, 0.0625]
            for s in scales:
                fractal += s * np.sin(x[i] / s) * np.cos(x[i] / (s * 3.0))
                
        # Dimensionality complexity with polynomial and exponential terms
        complexity = 0.0
        for i in range(self.dim):
            # Combination of polynomial and exponential terms with scaling factors
            complexity += (x[i]**6 + x[i]**5 + x[i]**4 + x[i]**3) * np.exp(-self.delta * abs(x[i]))
            
        # Global modulation based on solution quality and proximity to optima
        modulation = 0.0
        norm_x = np.linalg.norm(x)
        if norm_x < 0.3:
            modulation = 12.0 * np.exp(-norm_x**2)
        elif norm_x > 4.7:
            modulation = 10.0 * np.exp(-(norm_x - 4.7)**2)
            
        # Add chaotic noise for enhanced ergodicity
        chaos_noise = 0.0
        for i in range(self.dim):
            chaos_noise += self.epsilon * np.sin(x[i] * 12.0) * np.cos(x[i] * 18.0)
            
        # Combine all components with adaptive weights
        result = 1.3 * chaotic + 1.4 * harmonic + 1.1 * coupling + 0.8 * fractal + 0.9 * complexity + modulation + chaos_noise
        
        # Add offset to ensure positive fitness and scale appropriately
        return result + 15.0 * self.dim