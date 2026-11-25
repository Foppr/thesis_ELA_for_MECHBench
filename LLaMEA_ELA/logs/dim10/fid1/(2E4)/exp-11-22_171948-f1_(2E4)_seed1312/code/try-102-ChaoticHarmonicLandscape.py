import numpy as np

class ChaoticHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic phase coupling with logistic map modulation
        for i in range(self.dim):
            r = 3.9 + 0.1 * np.sin(0.1 * i)
            phase = np.pi * (i / self.dim) ** 3 + 0.5 * np.sin(r * x[i])
            freq = 2 ** (i % 7 + 1) + 0.3 * np.cos(x[i])
            harmonic = np.sin(freq * x[i] + phase) * np.exp(-0.15 * np.abs(x[i]))
            result += 0.6 * harmonic**2
        
        # Fractal-conditioned dynamic coupling between dimensions
        for i in range(self.dim - 1):
            coupling = np.sin(4 * (x[i] - x[i+1]) + 0.3 * np.sin(x[i])) * np.cos(3 * (x[i] + x[i+1]))
            fractal_factor = 1.0 + 0.2 * np.sin(np.log(np.abs(x[i]) + 1))
            result += 0.4 * coupling * fractal_factor
        
        # Adaptive ridge structure with chaotic curvature
        for i in range(self.dim):
            ridge_freq = 15 + i * 3 + 2 * np.sin(0.5 * i)
            ridge = np.sin(ridge_freq * x[i]) * np.exp(-0.03 * x[i]**2) * (1.0 + 0.1 * np.sin(x[i]))
            result += 0.8 * ridge**2
        
        # Multi-scale exponentially weighted cross-dimensional interactions with chaotic weights
        for i in range(self.dim - 1):
            weight = np.exp(-0.3 * (i + 1) + 0.1 * np.sin(0.2 * i))
            interaction = (x[i]**2 + x[i+1]**2) * np.sin(7 * (x[i] - x[i+1])) * (1.0 + 0.05 * np.cos(x[i]))
            result += weight * interaction
        
        # Ultra-high frequency oscillatory behavior with chaotic amplitude decay
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.2 * i + 0.05 * np.sin(0.3 * i))
            oscillation = np.sin(30 * x[i]) * np.cos(25 * x[i]) * scale
            result += 0.5 * oscillation**2
        
        # Chaotic adaptive conditioning based on local gradient magnitude and fractal curvature
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(np.cos(x[i]))
        chaos_factor = 1.0 + 0.6 * np.sin(np.log(np.abs(grad_magnitude) + 1))
        conditioning = 1.0 + 0.4 * np.tanh(grad_magnitude) * chaos_factor
        
        # Add higher-order polynomial interactions with chaotic coefficients
        poly_interaction = 0.0
        for i in range(self.dim - 2):
            coeff = 1.0 + 0.3 * np.sin(0.2 * i)
            poly_interaction += (x[i]**4 + x[i+1]**4 + x[i+2]**4) * np.sin(coeff * (x[i] + x[i+1] + x[i+2]))
        result += 0.15 * poly_interaction
        
        # Add fractal-like scaling to conditioning with chaotic modulation
        fractal_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 2) + 0.1 * np.cos(self.dim))
        conditioning *= fractal_scale
        
        result *= conditioning
        
        # Chaotic asymmetric basin structure with multi-scale symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 5) * np.sin(0.6 * x[i]) + 0.6 * (x[i] ** 4) * np.cos(0.4 * x[i])
        result += 0.3 * asymmetry
        
        # Multi-modal peak structure with chaotic heights and positions
        multimodal = 0.0
        for i in range(self.dim):
            height1 = 1.0 + 0.2 * np.sin(0.5 * i)
            height2 = 0.8 + 0.1 * np.cos(0.3 * i)
            pos1 = 2.0 + 0.5 * np.sin(0.4 * i)
            pos2 = -2.0 + 0.3 * np.cos(0.6 * i)
            multimodal += height1 * np.sin(12 * x[i]) * np.exp(-0.1 * (x[i] - pos1)**2) + height2 * np.cos(10 * x[i]) * np.exp(-0.1 * (x[i] - pos2)**2)
        result += 0.4 * multimodal
        
        # Final normalization and regularization with chaotic noise
        result /= self.dim
        result += 0.08 * np.sum(x**5) / self.dim
        
        # Add chaotic noise term to increase robustness testing
        noise = 0.02 * np.random.rand() * (1.0 + 0.1 * np.sin(np.log(self.dim + 1)))
        result += noise
        
        return result