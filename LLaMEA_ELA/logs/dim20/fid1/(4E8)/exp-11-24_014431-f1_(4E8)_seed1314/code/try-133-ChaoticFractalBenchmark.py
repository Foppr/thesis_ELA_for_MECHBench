import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic cosine wave components with dynamic frequencies and amplitudes
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(0.5 * i)
            amp = 0.8 + 0.2 * np.cos(0.3 * i)
            f_val += amp * np.cos(freq * x[i]) * (1 + 0.1 * np.sin(3 * x[i]))
        
        # Add adaptive polynomial conditioning with chaotic exponents
        for i in range(self.dim):
            exp = 2 + 1.5 * np.sin(0.4 * i)
            coeff = 0.1 + 0.05 * np.cos(0.6 * i)
            f_val += coeff * (x[i]**exp) * (1 + 0.15 * np.sin(2 * x[i]))
        
        # Add self-similar fractal components with recursive scaling
        scale = 0.2
        for k in range(1, 6):
            for i in range(self.dim):
                f_val += scale * np.cos(k * 15 * x[i]) * np.sin(k * 12 * x[i])
            scale *= 0.7
        
        # Add dynamic coupling terms with adaptive strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.1 + 0.05 * np.sin(0.3 * (i + j))
                f_val += strength * np.cos(3 * (x[i] - x[j])) * np.sin(2 * (x[i] + x[j]))
        
        # Add boundary-enhanced ruggedness
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                f_val += 10 * (abs(x[i]) - 4.0)**3
        
        # Add chaotic cubic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * (x[i]**3) * np.sin(2 * x[j]) + 0.03 * (x[j]**3) * np.cos(2 * x[i])
        
        # Add multi-scale harmonic modulation
        for i in range(self.dim):
            f_val += 0.1 * np.cos(8 * x[i]) * np.sin(6 * x[i]) * (1 + 0.2 * np.cos(4 * x[i]))
        
        # Add global sinusoidal modulation with varying phases
        phase = 0.5 * np.pi * np.sum(x)
        f_val += 0.15 * np.sin(phase) + 0.1 * np.cos(phase) + 0.08 * np.sin(2 * phase)
        
        return f_val