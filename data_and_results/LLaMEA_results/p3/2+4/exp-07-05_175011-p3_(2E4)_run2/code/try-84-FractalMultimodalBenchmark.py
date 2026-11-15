import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Fractal-like periodic components with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal += np.sin(10 * dist) * np.cos(5 * dist) * np.exp(-0.1 * dist**2)
        
        # Multi-scale sinusoidal interaction with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += np.sum([np.sin((2**k) * x_norm[i]) * np.cos((2**k) * x_norm[i]) for k in range(1, 5)])
        
        # Chaotic tent map inspired interaction terms
        tent_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tent_interaction += np.tanh(5 * (x_norm[i] + x_norm[j])) * np.sin(3 * (x_norm[i] - x_norm[j]))
        
        # Hyperbolic tangent based multimodal structure
        hyperbolic = np.sum(np.tanh(3 * x_norm)**2 + np.tanh(7 * x_norm)**4)
        
        # Cross-dimensional coupling with phase-shifted trigonometric terms
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(x_norm[i] + x_norm[i+1] + 0.7) * np.cos(x_norm[i] - x_norm[i+1] - 0.4)
        
        # Global optimum shifted to a high-fitness region with fractal perturbation
        optimum_shift = np.sum(np.sin(15 * x_norm)**2 + np.cos(15 * x_norm)**2 + 0.2 * np.sin(40 * x_norm))
        
        # Additional chaotic component with non-linear scaling
        chaotic = np.sum(np.sin(30 * x_norm) * np.cos(20 * x_norm) * np.exp(-0.5 * np.abs(x_norm)))
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.2 * fractal + 1.8 * multi_scale + 0.9 * tent_interaction + 1.5 * hyperbolic + 0.7 * coupling + 1.6 * optimum_shift + 0.5 * chaotic