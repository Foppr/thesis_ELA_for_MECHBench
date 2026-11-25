import numpy as np

class QuaternionSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.hurst = 0.3
        self.fractal_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic quaternion dynamics component
        quat_term = 0.0
        for i in range(self.dim):
            # Quaternion-like interaction with chaotic modulation
            q_real = np.sin(x[i]) * np.cos(0.5 * x[i])
            q_imag1 = np.cos(x[i]) * np.sin(0.3 * x[i])
            q_imag2 = np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            q_imag3 = np.cos(0.6 * x[i]) * np.sin(0.8 * x[i])
            
            # Combine quaternion components with chaotic scaling
            quat_val = q_real**2 + q_imag1**2 + q_imag2**2 + q_imag3**2
            quat_term += quat_val * (1.0 + 0.3 * np.sin(0.5 * i + 0.2 * np.sum(x**2)))
            
        # Adaptive radial conditioning
        radial_term = 0.0
        for i in range(self.dim):
            # Radial scaling with adaptive parameters
            r = np.abs(x[i])
            radial_factor = 1.0 + 0.5 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            radial_term += radial_factor * (r**2 + 0.1 * r**4 + 0.01 * r**6)
            
        # Multi-scale harmonic interactions
        harmonic_term = 0.0
        for i in range(self.dim):
            # Multiple harmonic frequencies with varying amplitudes
            freq1 = 1.0 + 0.5 * np.sin(0.3 * i)
            freq2 = 2.0 + 0.8 * np.cos(0.4 * i)
            amp1 = 1.0 + 0.4 * np.sin(0.5 * i + 0.2 * np.sum(x**2))
            amp2 = 0.8 + 0.3 * np.cos(0.6 * i + 0.1 * np.sum(x**2))
            
            harmonic_term += amp1 * np.sin(freq1 * x[i]) * np.cos(freq1 * x[i] + 0.5) + \
                           amp2 * np.sin(freq2 * x[i]) * np.cos(freq2 * x[i] + 0.3)
            
        # Gradient-based saddle-point interactions with modified coupling
        saddle_term = 0.0
        for i in range(self.dim):
            grad_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = x[i] - x[j]
                    # Modified coupling strength and phase shift
                    coupling = 1.2 + 0.4 * np.sin(0.3 * (i + j) + 0.5 * np.sum(x**2))
                    phase_shift = 0.3 * np.cos(0.2 * i + 0.1 * j)
                    grad_sum += coupling * diff / (1.0 + diff**2 + phase_shift)
            saddle_term += grad_sum * np.sin(0.7 * x[i] + 0.4 * np.cos(x[i]))
            
        # Boundary repulsion with enhanced fractal scaling
        boundary_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist_from_boundary = 5.0 - np.abs(x[i])
                penalty = 2.0 * dist_from_boundary**3.0
                # Enhanced fractal scaling
                fractal_factor = 1.0 + 0.2 * np.sin(0.8 * x[i])
                boundary_term += penalty * fractal_factor * np.exp(-0.15 * x[i]**2)
                
        # Cross-dimensional coupling with phase-shifted weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Phase-shifted coupling weights
                weight = 1.0 + 0.6 * np.sin(0.2 * (i + j) + 0.4 * np.sum(x**2) + 0.5 * np.cos(x[i] * x[j]))
                phase_shift = 0.4 * np.sin(0.3 * x[i] + 0.2 * x[j])
                coupling_term += weight * (x[i]**2 + x[j]**2) * np.cos(x[i] - x[j] + phase_shift)
                
        # Global conditioning with spectral modulation
        r = np.sqrt(np.sum(x**2))
        global_factor = 1.0 + 0.4 * np.sin(0.6 * r + 0.3 * np.cos(r))
        
        # Combine all terms
        total = quat_term + radial_term + harmonic_term + saddle_term + boundary_term + coupling_term
        return total * global_factor
        
    def _fractal_brownian_motion(self, x, hurst):
        """Simple approximation of fractal Brownian motion"""
        return np.sin(x) * np.cos(0.5 * x) * np.exp(-0.1 * np.abs(x)) * (1.0 + 0.2 * np.sin(2.0 * x))