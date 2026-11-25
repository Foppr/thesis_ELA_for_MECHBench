import numpy as np

class ChaoticLogarithmicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested logarithmic potential terms with dynamic scaling
        f1 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.7 * np.sin(0.8 * i)
            if x[i] == 0:
                f1 += 15.0
            else:
                f1 += scale * np.log(np.abs(x[i]) + 1e-8) * np.exp(-0.15 * x[i]**2)
                
        # Dynamic radial saddle point with time-varying modulation
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.4 * np.sin(0.6 * i * r + 0.5 * r)
            f2 += mod * x[i]**2 * (x[i]**2 - 1.5) * np.exp(-0.08 * r**2)
            
        # Cross-dimensional cubic coupling with stochastic weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.6 + 0.4 * np.cos(0.4 * (i + j) + 0.3 * r)
                f3 += weight * x[i]**3 * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Boundary-repelling harmonic terms with dynamic frequencies
        f4 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(0.5 * i)
            if x[i] < -4.0:
                f4 += 2.5 * np.cos(freq * (x[i] + 5.0)) * np.exp(-0.12 * (x[i] + 5.0)**2)
            elif x[i] > 4.0:
                f4 += 2.5 * np.cos(freq * (x[i] - 5.0)) * np.exp(-0.12 * (x[i] - 5.0)**2)
                
        # Multi-scale chaotic oscillations with adaptive amplitudes
        f5 = 0.0
        for i in range(self.dim):
            freq = 2.5 + 2.0 * np.sin(0.4 * i + 0.3 * r)
            amp = 1.2 + 0.9 * np.cos(0.3 * i + 0.2 * r)
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.04 * np.abs(x[i]))
            
        # Asymmetric radial harmonic with stochastic amplitude and phase
        f6 = 0.0
        for k in range(1, 8):
            amp = 0.6 + 0.4 * np.sin(0.7 * k + 0.3 * r)
            phase = 0.3 * np.cos(0.5 * k + 0.2 * r)
            f6 += amp * np.cos(k * r + phase) * np.exp(-0.05 * r**2)
            
        # Saddle-point inducing quartic terms with adaptive boundary effects
        f7 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f7 += 0.6 * (x[i]**4 - 2.5 * x[i]**2) * np.exp(-0.03 * x[i]**2)
            else:
                f7 += 0.6 * (x[i]**4 - 2.5 * x[i]**2) * np.exp(-0.03 * x[i]**2)
                
        # Cross-dimensional chaotic interaction with exponential scaling and stochastic coupling
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_factor = 1.0 + 0.5 * np.sin(0.6 * i * j + 0.4 * r)
                coupling = np.exp(-0.12 * (x[i]**2 + x[j]**2)) * chaos_factor
                f8 += coupling * (x[i] * x[j])**2
                
        # Adaptive conditioning with logarithmic scaling and dynamic exponent
        f9 = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.4 * np.sin(0.7 * i + 0.3 * r)
            exp_factor = 0.8 + 0.2 * np.cos(0.5 * i + 0.4 * r)
            f9 += cond * np.log(np.abs(x[i]) + 1.0) * np.exp(-exp_factor * x[i]**2)
            
        # Fractal-like radial component with stochastic frequency modulation and time-varying amplitude
        f10 = 0.0
        for k in range(1, 10):
            freq_mod = 1.0 + 0.4 * np.sin(0.8 * k + 0.3 * r)
            amp_mod = 0.9 + 0.1 * np.cos(0.6 * k + 0.2 * r)
            f10 += amp_mod * np.cos(freq_mod * r) * np.exp(-0.04 * r**2) / (k + 1.0)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10