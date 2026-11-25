import numpy as np

class QuaternionExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic radial potentials with dynamic decay rates
        r = np.sqrt(np.sum(x**2))
        f1 = 0.0
        for i in range(self.dim):
            decay = 0.3 + 0.7 * np.sin(0.4 * i + 0.2 * r)
            f1 += np.exp(-decay * (x[i]**2)) * (1.0 + 0.4 * np.cos(0.5 * i + 0.3 * r))
            
        # Quaternion-inspired cross-dimensional terms with phase rotation
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Imaginary-like coupling with dynamic phase rotation
                phase = 0.4 * np.pi * (i / self.dim) + 0.2 * r
                real_part = np.cos(x[i] * x[j])
                imag_part = np.sin(x[i] * x[j])
                coupling = 0.3 + 0.7 * np.cos(0.2 * (i + j) + 0.1 * r)
                f2 += coupling * (real_part * np.cos(phase) - imag_part * np.sin(phase)) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Adaptive noise modulation with chaotic amplitude scaling
        f3 = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.6 * np.cos(0.4 * i + 0.1 * r)
            freq = 1.5 + 2.5 * np.sin(0.3 * i + 0.1 * r)
            noise = amp * np.cos(freq * x[i] + 0.4 * r) * np.exp(-0.03 * x[i]**2)
            f3 += noise
            
        # Multi-scale exponential interactions with radial conditioning
        f4 = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.6 * np.cos(0.4 * i + 0.2 * r)
            f4 += scale * np.exp(-0.3 * (x[i] / (1.0 + 0.4 * np.abs(x[i])))**2) * np.sin(0.4 * x[i])
            
        # Boundary repulsion with logarithmic scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 1.2 * np.log(1.0 - x[i]/5.0)**2 + 0.3 * np.exp(-x[i]**2 / 8.0)
            else:
                penalty = 1.2 * np.log(1.0 + x[i]/5.0)**2 + 0.3 * np.exp(-x[i]**2 / 8.0)
            f5 += penalty
            
        # Chaotic coupling with cosine and sine combinations
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 + 0.8 * np.sin(0.3 * (i - j) + 0.1 * r)
                f6 += coupling * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Polynomial chaos with variable coefficients
        f7 = 0.0
        for i in range(self.dim):
            coeff1 = 0.9 + 0.3 * np.sin(0.4 * i)
            coeff2 = 0.7 + 0.3 * np.cos(0.3 * i)
            coeff3 = 0.6 + 0.2 * np.sin(0.5 * i)
            f7 += coeff1 * x[i]**4 + coeff2 * x[i]**3 + coeff3 * x[i]**2
            
        # Radial harmonic oscillations with variable frequency
        f8 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.5 * np.cos(0.3 * i + 0.1 * r)
            f8 += np.sin(freq * x[i]) * np.exp(-0.04 * x[i]**2)
            
        # Cross-dimensional exponential coupling with phase modulation
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.2 + 0.5 * np.cos(0.4 * (i * j) + 0.1 * r)
                f9 += mod * np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(0.3 * (x[i] + x[j]))
                
        # Hyper-spherical harmonic interactions with dynamic coupling
        f10 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    # Triple harmonic coupling with radial dependence
                    coupling = 0.25 + 0.4 * np.sin(0.2 * (i + j + k) + 0.05 * r)
                    phase = 0.3 * np.pi * (i / self.dim) * (j / self.dim)
                    f10 += coupling * np.cos(x[i] * x[j] * x[k]) * np.cos(phase) * np.exp(-0.01 * (x[i]**2 + x[j]**2 + x[k]**2))
                    
        # Enhanced multi-modal structure with fractal-like frequency modulation
        f11 = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.8 * np.sin(0.5 * i + 0.3 * r) * np.cos(0.4 * i)
            f11 += freq_mod * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Cross-dimensional exponential coupling with radial amplitude modulation
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                amp_mod = 1.3 + 0.7 * np.sin(0.3 * (i + j) + 0.1 * r)
                f12 += amp_mod * np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(0.4 * (x[i] + x[j]))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12