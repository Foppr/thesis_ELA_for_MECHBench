import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-order polynomial with chaotic scaling factors and fractal-like exponentiation
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.3 * np.abs(x[i]))
            exp_factor = 1.0 + 0.2 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            poly_term += 0.5 * (x[i] ** (5.0 + exp_factor)) * scale * np.exp(-0.4 * x[i]**2)
        
        # Multi-scale logarithmic coupling with variable weights and chaotic modulation
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.4 * (1.0 + np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]))
                # Chaotic modulation of the coupling strength
                chaos_mod = 1.0 + 0.1 * np.sin(3.0 * x[i] + 2.0 * x[j])
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j]) * chaos_mod
        
        # Quaternion-inspired rotational symmetry with dynamic phase modulation and multi-fractal scaling
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                freq = 4.0 + 2.0 * np.sin(0.5 * x[i]) + 1.5 * np.cos(0.7 * x[j])
                # Enhanced chaotic phase shift with fractal-like behavior
                phase = 0.8 * np.sin(0.4 * x[i] + 0.8 * x[j]) + 0.3 * np.sin(1.5 * x[i] * x[j]) + 0.1 * np.cos(2.0 * x[i] + x[j])
                # Multi-fractal scaling factor
                fractal_scale = 1.0 + 0.1 * np.sin(5.0 * x[i])
                rot_term += 0.3 * np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]) + phase) * fractal_scale
        
        # Multi-scale exponential decay with chaotic frequency modulation and variable damping
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.4, 1.3, 2.8, 5.7, 7.9, 10.1]
            decay = 0.0
            for f in freqs:
                # Adjusted exponential decay frequencies with multi-fractal modulation
                mod_freq = f * (1.0 + 0.5 * np.sin(1.3 * x[i]) * np.cos(1.0 * x[i]))
                # Fractal-like damping factor
                damp_factor = 1.0 + 0.2 * np.sin(4.0 * x[i])
                decay += np.exp(-mod_freq * np.abs(x[i]) * damp_factor) * np.sin(mod_freq * x[i]) * (1.0 + 0.15 * np.sin(0.6 * x[i]))
            decay_term += 0.3 * decay
        
        # Basin boundary with irregular fractal-like irregularities and multi-scale noise injection
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.2:
                basin_term += 0.15 * x[i]**5 + 0.05 * np.sin(20 * x[i]) + 0.04 * np.random.rand() + 0.02 * np.sin(30 * x[i])
            else:
                # Fractal-like basin structure
                fractal_basin = 0.18 * np.abs(x[i])**2.8 + 0.06 * np.cos(10 * x[i]) + 0.03 * np.random.rand()
                # Multi-scale noise injection
                noise_injection = 0.01 * np.sin(50 * x[i]) + 0.01 * np.cos(40 * x[i])
                basin_term += fractal_basin + noise_injection
        
        # Chaotic sine-wave component with adaptive amplitude and multi-fractal modulation
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.7 + 0.3 * np.sin(0.9 * x[i]) + 0.1 * np.cos(2.5 * x[i])
            # Multi-fractal frequency modulation
            freq_mod = 1.0 + 0.2 * np.sin(4.0 * x[i])
            chaos_term += amp * np.sin(200 * x[i] * freq_mod) * np.exp(-0.9 * x[i]**2)
        
        # Enhanced ridge structure with multi-scale harmonic components and chaotic phase shifts
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.15 * np.sin(3.5 * x[i]) * np.cos(2.8 * x[i]) + 0.07 * np.sin(7.5 * x[i]) + 0.03 * np.sin(12.0 * x[i])
        
        # Add novel noise injection mechanism for increased algorithm discrimination
        noise_injection = 0.0
        for i in range(self.dim):
            noise_injection += 0.05 * np.random.randn() * np.exp(-0.5 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term + ridge_term + noise_injection