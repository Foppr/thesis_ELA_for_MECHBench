import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Sinusoidal interaction terms with varying frequencies and amplitudes
        sinusoidal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Pairwise sinusoidal interaction with frequency scaling
                freq = 2.0 + 0.5 * np.sin(i * 0.7) + 0.3 * np.cos(j * 0.4)
                amp = 1.0 + 0.2 * np.sin(i * 0.3) * np.cos(j * 0.5)
                sinusoidal += amp * np.sin(freq * (x_normalized[i] + x_normalized[j]))
        
        # Polynomial coupling with varying degrees
        polynomial = 0
        for i in range(self.dim):
            # Higher-order polynomial terms with random coefficients
            poly_term = 0
            for deg in range(3, 7):
                coeff = 0.1 + 0.05 * np.sin(i * 0.2 + deg)
                poly_term += coeff * (x_normalized[i] ** deg)
            polynomial += poly_term
            
        # Fractal-like self-similarity using recursive scaling
        fractal = 0
        for i in range(self.dim):
            # Create self-similar structure using nested sine waves
            scale = 1.0
            for level in range(1, 4):
                scale *= 0.5
                fractal += scale * np.sin(2**(level) * x_normalized[i])
                
        # Add a global periodic modulation to increase complexity
        global_mod = 0
        for i in range(self.dim):
            global_mod += np.sin(0.5 * x_normalized[i]) * np.cos(0.3 * x_normalized[i])
            
        # Combine all components with different weights
        result = 0.25 * f1 + 0.3 * sinusoidal + 0.2 * polynomial + 0.15 * fractal + 0.1 * global_mod
        
        # Add small random noise to prevent algorithm from memorizing
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x_normalized)
        result += noise
        
        return result