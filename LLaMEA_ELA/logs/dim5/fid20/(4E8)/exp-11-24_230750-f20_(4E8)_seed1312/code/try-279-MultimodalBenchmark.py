import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quantum harmonic oscillator with chaotic modulation
        quantum = 0.0
        for i in range(self.dim):
            quantum += (np.sin(x[i]) * np.cos(x[i])) ** 2 + 0.1 * x[i] ** 4 + 0.05 * np.sin(10 * x[i]) * np.cos(10 * x[i])
        
        # Adaptive fractal landscape with dynamic scaling and multi-resolution structure
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2 ** (i+1) * x[i]) * np.cos(2 ** (i+1) * x[i]) + 0.3 * np.sin(3 * 2 ** (i+1) * x[i])
        
        # Multi-scale Gaussian peaks with time-varying centers and dynamic widths
        gaussian = 0.0
        scales = [1.0, 0.5, 2.0, 0.25]
        for i in range(self.dim):
            for scale in scales:
                center = scale * np.sin(x[i]) + 0.1 * np.cos(5 * x[i])
                width = 0.5 + 0.5 * np.cos(x[i]) + 0.1 * np.sin(3 * x[i])
                gaussian += np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2))
        
        # Enhanced cross-dimensional coupling with chaotic interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                interaction = np.exp(-0.5 * ((x[i] - x[j]) ** 2)) * (x[i] ** 2 + x[j] ** 2)
                chaotic_term = 0.2 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                cross += interaction + chaotic_term
        
        # Dynamic multi-scale resonance peaks with fractional Brownian motion inspired components
        resonance = 0.0
        for i in range(self.dim):
            resonance += np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.log(np.abs(x[i]) + 1) + 0.1 * np.sin(15 * x[i])
        
        # Asymmetric gradient deception with polynomial-trigonometric hybrid mixing
        deception = 0.0
        for i in range(self.dim):
            deception += (x[i] ** 3 - 2 * x[i] ** 2 + x[i]) * np.sin(x[i]) + 0.15 * np.cos(7 * x[i]) * np.sin(4 * x[i])
        
        # Additional chaotic component with hyperbolic tangent oscillations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.tanh(5 * x[i]) * np.sin(8 * x[i]) + 0.2 * np.cos(12 * x[i])
        
        # Combine all components with varying weights and add noise
        result = (0.2 * quantum + 0.15 * fractal + 0.25 * gaussian + 0.2 * cross + 
                 0.1 * resonance + 0.1 * deception + 0.05 * chaotic)
        
        # Add small random noise to increase robustness
        result += 0.001 * np.random.randn()
        
        return result