import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for sine map dynamics
        self.omega_values = np.linspace(0.5, 2.0, dim)
        self.q_values = np.linspace(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sine map components with quantum-like interference
        for i in range(self.dim):
            # Sine map with quantum phase modulation
            sine_val = np.sin(self.omega_values[i] * x[i])
            phase = np.cos(self.q_values[i] * np.sum(x[:i]) if i > 0 else 0)
            f_val += 0.4 * sine_val * phase + 0.1 * np.sin(3 * sine_val) * np.cos(2 * phase)
            
        # Add quantum harmonic oscillator terms with position-dependent frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(x[i] * 0.5)
            f_val += 0.3 * (x[i]**2) * freq + 0.2 * np.cos(x[i] * freq)
            
        # Add memory-dependent coupling terms with exponential decay
        for i in range(self.dim):
            if i > 0:
                memory_weight = np.exp(-0.1 * i)
                f_val += memory_weight * (x[i] - x[i-1])**4 + 0.15 * np.abs(x[i] - x[i-1])**2.5
                
        # Add fractal-like self-similar modulations
        for i in range(self.dim):
            f_val += 0.2 * np.sin(2**i * x[i]) * np.cos(3**i * x[i]) + \
                     0.1 * np.sin(5**i * x[i]) * np.cos(7**i * x[i])
                     
        # Add complex polynomial coupling with fractional exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                frac_exp = 0.5 + 0.3 * np.sin(i * 0.2)
                f_val += 0.1 * (x[i]**frac_exp) * (x[j]**(2 - frac_exp)) + \
                         0.08 * x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Add time-delayed chaotic feedback with varying delays
        for i in range(self.dim):
            if i > 2:
                delay_term = np.sin(x[i-3] * 0.7) * np.cos(x[i-2] * 0.8)
                f_val += 0.12 * delay_term * x[i] + 0.05 * np.tan(delay_term)
                
        # Add a final fractal energy landscape with recursive scaling
        f_val += 0.15 * np.sin(np.sum(x**4)) + 0.1 * np.cos(np.prod(x) * 0.3) + \
                 0.08 * np.sin(np.sum(np.abs(x)**3))
        
        return f_val