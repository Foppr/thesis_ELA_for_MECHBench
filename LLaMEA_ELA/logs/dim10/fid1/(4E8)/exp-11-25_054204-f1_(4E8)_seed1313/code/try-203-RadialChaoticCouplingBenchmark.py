import numpy as np

class RadialChaoticCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic phases for dynamic modulation
        self.chaotic_phases = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with dynamic centers
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(self.chaotic_phases[i])
            rbf += np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.1 * self.chaotic_phases[i]))**2)
        
        # Polynomial coupling with chaotic weights
        poly_coupling = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(self.chaotic_phases[i] * x[i])
            poly_coupling += weight * (x[i]**3) * np.cos(0.5 * x[i])
            
        # Chaotic phase modulation with sine-cosine interactions
        phase_mod = 0.0
        for i in range(self.dim - 1):
            phase_mod += np.sin(x[i] + x[i+1]) * np.cos(x[i] * x[i+1] * self.chaotic_phases[i])
            
        # Dynamic radial harmonic component
        radial_harmonic = 0.0
        for i in range(self.dim):
            radial_harmonic += (x[i]**2) * np.sin(2.0 * x[i] + self.chaotic_phases[i]) * np.cos(x[i])
            
        # Cross-dimensional exponential coupling with dynamic scaling
        exp_coupling = 0.0
        for i in range(self.dim - 1):
            scale = 1.0 + 0.3 * np.cos(self.chaotic_phases[i] * self.chaotic_phases[i+1])
            exp_coupling += scale * np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(x[i] * x[i+1])
            
        # Multi-scale chaotic oscillation
        multi_scale = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.sin(self.chaotic_phases[i] * 3.0)
            multi_scale += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.tan(0.5 * x[i])
            
        # Fractional polynomial component with chaotic modulation
        frac_poly = 0.0
        for i in range(self.dim):
            frac_exp = 1.5 + 0.5 * np.sin(self.chaotic_phases[i] * 2.0)
            frac_poly += (x[i]**frac_exp) * np.cos(x[i] * self.chaotic_phases[i])
            
        # Sine-cosine interaction with dynamic frequency
        sincos_interaction = 0.0
        for i in range(self.dim - 1):
            freq = 2.0 + 1.5 * np.sin(self.chaotic_phases[i] + self.chaotic_phases[i+1])
            sincos_interaction += np.sin(freq * x[i]) * np.cos(freq * x[i+1])
            
        # Combined chaotic scaling factor
        scale_factor = 1.0 + 0.2 * np.sum(np.sin(self.chaotic_phases))
        
        return scale_factor * (rbf + poly_coupling + phase_mod + radial_harmonic + 
                              exp_coupling + multi_scale + frac_poly + sincos_interaction)