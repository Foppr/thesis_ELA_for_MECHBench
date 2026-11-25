import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired phase interactions with complex amplitude modulation
        quantum_phase = 0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.3 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            phase = np.exp(1j * (x[i] + 0.5 * np.sin(2 * x[i])))
            quantum_phase += amp_mod * np.real(phase * np.exp(1j * 3 * x[i]))
        
        # Adaptive neural network-like couplings with dynamic weights
        nn_coupling = 0
        for i in range(self.dim):
            weight = 1.0 + 0.2 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i]**2)
            activation = np.tanh(weight * x[i])
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                coupling = weight * np.exp(-dist**2) * np.sin(5 * dist)
                nn_coupling += coupling * activation
        
        # Fractal-based frequency modulation with multi-scale chaos
        fractal_freq = 0
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[i]**2)
            freq_mod += 0.8 * np.sin(0.1 * x[i]**3) * np.cos(0.4 * x[i])
            fractal_freq += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**2)
        
        # Spherical harmonic couplings with variable degree and order
        sph_harm = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x[i]**2 + x[j]**2)
                # Variable spherical harmonic terms
                degree = int(2 + 3 * np.sin(0.5 * x[i]))
                order = int(1 + 2 * np.cos(0.3 * x[j]))
                sph_term = (np.sin(degree * dist) * np.cos(order * dist) + 
                           0.7 * np.cos(degree * dist) * np.sin(order * dist)) / (dist + 1e-8)
                sph_harm += sph_term * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Hyperbolic tangent-based cross-dimensional interactions
        tanh_cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                tanh_cross += np.tanh(x[i] + x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric power-law with dynamic exponent
        power_scale = 0
        for i in range(self.dim):
            exp_factor = 2.0 + 0.8 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i]**2)
            asym_factor = 1.0 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.2 * x[i])
            power_scale += (np.abs(x[i])**exp_factor) * asym_factor * np.exp(-0.03 * x[i]**2)
        
        # Logarithmic fractal coupling with periodic modulation
        log_fractal = 0
        for i in range(self.dim):
            period_mod = 1.0 + 0.3 * np.sin(0.5 * x[i])
            log_term = np.log(np.abs(x[i]) + 1.0) * np.sin(period_mod * x[i])
            log_fractal += log_term * np.exp(-0.1 * x[i]**2)
        
        # Global conditioning with dynamic scaling factor
        cond_factor = 1.0 + 0.3 * np.sin(self.dim * 0.3) + 0.2 * np.cos(self.dim * 0.15)
        
        # Combine all components with optimized weights
        return cond_factor * (0.2 * quantum_phase + 0.25 * nn_coupling + 
                             0.2 * fractal_freq + 0.15 * sph_harm + 
                             0.1 * tanh_cross + 0.08 * power_scale + 0.02 * log_fractal)