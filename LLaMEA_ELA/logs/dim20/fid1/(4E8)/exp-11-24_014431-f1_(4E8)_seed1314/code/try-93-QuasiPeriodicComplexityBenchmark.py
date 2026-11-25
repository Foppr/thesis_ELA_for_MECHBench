import numpy as np

class QuasiPeriodicComplexityBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quasiperiodic frequencies for stability
        self.frequencies = [1.0 + i * 0.3 + np.sqrt(2) for i in range(dim)]
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add quasiperiodic trigonometric components with varying amplitudes and phases
        for i in range(self.dim):
            f_val += (0.8 + 0.2 * np.sin(x[i])) * np.cos(self.frequencies[i] * x[i]) + \
                     (0.6 + 0.1 * np.cos(x[i])) * np.sin(self.frequencies[i] * x[i])
        
        # Add polynomial conditioning with variable exponents and adaptive coefficients
        for i in range(self.dim):
            exp_factor = 2 + 0.5 * np.sin(0.5 * i)
            coef = 0.1 + 0.05 * np.cos(0.3 * i)
            f_val += coef * (x[i] ** exp_factor)
        
        # Add cross-dimensional coupling with quasiperiodic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_freq = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                f_val += 0.05 * np.cos(coupling_freq * (x[i] + x[j])) * \
                         np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add multi-scale harmonic modulation with fractal-like scaling
        for scale in range(1, 6):
            for i in range(self.dim):
                f_val += 0.03 * np.sin(scale * self.frequencies[i] * x[i]) * \
                         np.cos(scale * 0.7 * self.frequencies[i] * x[i])
        
        # Add boundary penalties with quasiperiodic penalty strengths
        for i in range(self.dim):
            penalty_strength = 1.0 + 0.3 * np.sin(0.4 * i)
            if abs(x[i]) > 4.0:
                f_val += penalty_strength * (abs(x[i]) - 4.0)**2
        
        # Add global quasiperiodic modulation
        global_mod = np.sum([np.sin(0.1 * i * x[i]) for i in range(self.dim)])
        f_val += 0.2 * np.cos(global_mod)
        
        return f_val