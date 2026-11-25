import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quaternion-like coupling parameters
        self.quat_coeffs = np.random.rand(min(dim, 15)) * 2.0 - 1.0
        # Dynamic phase modulation frequencies
        self.phase_freqs = np.linspace(0.3, 4.0, min(dim, 15))
        # Fractal potential well scaling
        self.fractal_scales = np.logspace(-1, 1, min(dim, 15))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-inspired coupling with hyperchaotic feedback
        quat_coupling = 0.0
        for i in range(self.dim):
            if i >= len(self.quat_coeffs):
                break
            # Use quaternion-like interaction terms
            q_real = np.cos(x[i] * self.quat_coeffs[i % len(self.quat_coeffs)])
            q_imag = np.sin(x[i] * self.quat_coeffs[i % len(self.quat_coeffs)])
            quat_coupling += q_real * q_imag
            
        # Dynamic phase modulation with time-varying coupling
        phase_mod = 0.0
        for i in range(self.dim):
            if i >= len(self.phase_freqs):
                break
            phase = np.sin(self.phase_freqs[i % len(self.phase_freqs)] * x[i])
            phase_mod += phase * np.cos(2.0 * x[i]**2 + 0.5 * i)
            
        # Multi-scale fractal potential wells with varying depth
        fractal_pot = 0.0
        for i in range(self.dim):
            if i >= len(self.fractal_scales):
                break
            scale = self.fractal_scales[i % len(self.fractal_scales)]
            # Create fractal-like potential with exponential decay
            fractal_pot += np.exp(-scale * np.abs(x[i])) * np.sin(scale * x[i]**2)
            
        # Adaptive ridge structure with hyperbolic tangent curvature
        adaptive_ridge = 0.0
        for i in range(self.dim):
            # Dynamic ridge parameters based on dimension
            ridge_height = 1.0 + 0.5 * np.sin(0.3 * i + self.dim * 0.15)
            ridge_width = 0.5 + 0.3 * np.cos(0.2 * i + self.dim * 0.1)
            position = -4.0 + 8.0 * (i / max(1, self.dim - 1))
            adaptive_ridge += ridge_height * np.tanh((x[i] - position) / ridge_width)**2
            
        # Asymmetric hyperbolic component with dynamic exponent
        asym_hyper = 0.0
        for i in range(self.dim):
            exp_factor = 1.5 + 0.5 * np.sin(0.4 * i)
            asym_hyper += np.abs(x[i])**exp_factor * np.cos(0.3 * x[i]**2)
            
        # Combine all components with dynamic weighting
        dim_factor = 1.0 + 0.05 * np.log(self.dim + 1)
        return (0.22 * quat_coupling + 0.25 * phase_mod + 
                0.23 * fractal_pot + 0.18 * adaptive_ridge + 0.12 * asym_hyper) * dim_factor