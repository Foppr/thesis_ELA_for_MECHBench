import numpy as np

class FractalEllipticalSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_noise_scale = 0.5
        self.elliptical_aspect_ratio = 2.0
        self.spectral_coupling_strength = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal noise field component
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal noise with varying amplitudes
            noise_val = 0.0
            for scale in [1, 2, 4]:
                freq = scale * 2.0
                amp = self.fractal_noise_scale / scale
                noise_val += amp * np.sin(freq * x[i] + np.cos(freq * x[i]))
            
            # Position-dependent fractal modulation
            pos_mod = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * np.sum(x**2))
            fractal_term += noise_val * pos_mod
            
        # Adaptive elliptical conditioning
        elliptical_term = 0.0
        for i in range(self.dim):
            # Elliptical distortion with adaptive axes
            axis_ratio = self.elliptical_aspect_ratio + 0.5 * np.sin(0.3 * i + 0.1 * np.sum(x**2))
            dist_from_center = x[i]**2 / (axis_ratio**2 + 0.1)
            elliptical_term += dist_from_center
            
        # Spectral coupling interactions
        spectral_term = 0.0
        for i in range(self.dim):
            # Coupling with frequency domain interactions
            freq_coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.spectral_coupling_strength * np.cos(0.2 * (i - j))
                    freq_coupling += coupling_strength * np.sin(x[i] + x[j])
                    
            spectral_term += freq_coupling * np.cos(0.3 * x[i] + 0.4 * np.sum(x**2))
            
        # Dynamic curvature modulation
        curvature_term = 0.0
        for i in range(self.dim):
            # Adaptive curvature with phase-shifted modulations
            phase_shift = 0.5 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            curvature = 1.0 + 0.4 * np.cos(0.6 * x[i] + phase_shift)
            curvature_term += curvature * x[i]**4
            
        # Boundary interaction with adaptive repulsion
        boundary_term = 0.0
        for i in range(self.dim):
            # Distance from boundaries with variable penalty
            dist_to_boundary = min(np.abs(x[i]) - 4.0, 0.0)
            if dist_to_boundary < 0:
                penalty = np.abs(dist_to_boundary)**2.5 * (1.0 + 0.3 * np.sin(0.7 * x[i]))
                boundary_term += penalty
                
        # Cross-dimensional interaction with dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on position and dimension
                weight = 1.0 + 0.5 * np.sin(0.3 * (i + j) + 0.2 * np.sum(x**2))
                cross_term += weight * (x[i] - x[j])**2
                
        # Global scaling with spectral modulation
        r = np.sqrt(np.sum(x**2))
        global_scale = 1.0 + 0.3 * np.sin(0.5 * r + 0.2 * np.cos(r))
        
        # Combine all terms
        total = fractal_term + elliptical_term + spectral_term + curvature_term + boundary_term + cross_term
        return total * global_scale