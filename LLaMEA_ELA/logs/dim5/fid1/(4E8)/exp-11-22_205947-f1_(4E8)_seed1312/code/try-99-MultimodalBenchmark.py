import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic parameters for phase modulation and coupling
        self.phase_shifts = np.linspace(0, 2*np.pi, dim, endpoint=False)
        self.coupling_strength = 0.5 + 0.3 * np.sin(np.arange(dim) * 0.7)
        self.adaptive_scaling = 1.0 + 0.2 * np.cos(np.arange(dim) * 0.4)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient component with implicit constraint
        grad_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced constraint via multi-term modulation
            constraint_term = np.sin(xi) * np.cos(xi) * np.tanh(xi)
            grad_component += (xi**5 + 2*xi**4 + xi**3 + 0.5*xi**2) * constraint_term
            
        # Dynamic phase-shifted trigonometric terms with adaptive weights
        phase_component = 0.0
        for i in range(self.dim):
            phase = self.phase_shifts[i]
            weight = self.adaptive_scaling[i]
            phase_component += weight * np.sin(5.0 * x[i] + phase) * np.cos(7.0 * x[i] + phase)
            
        # Non-linear coupling with dynamic weights and enhanced interaction
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = self.coupling_strength[i] * self.coupling_strength[j]
                coupling_component += weight * (x[i]**3 + x[j]**3) * np.sin(2.0 * (x[i] - x[j]))
                
        # Sharp multimodal peaks with adaptive scaling and multiple harmonics
        peak_component = 0.0
        for i in range(self.dim):
            # Multiple sharp peaks at different scales with harmonic modulation
            peak_component += 0.6 * np.exp(-0.5 * ((x[i] - 2.0)**2)) + \
                             0.4 * np.exp(-0.5 * ((x[i] + 2.0)**2)) + \
                             0.3 * np.exp(-0.5 * ((x[i] - 4.0)**2)) + \
                             0.2 * np.exp(-0.5 * ((x[i] + 4.0)**2))
        
        # Smooth radial basis with dynamic centers and variable widths
        rbf_component = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.6)
            width = 1.2 + 0.3 * np.cos(i * 0.4)
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Add a global scaling factor based on dimension with enhanced conditioning
        scale_factor = 1.0 + 0.15 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * 0.3)
        
        # Combine all components with refined weights for better balance
        total = (0.35 * grad_component + 
                0.25 * phase_component + 
                0.2 * coupling_component + 
                0.15 * peak_component + 
                0.05 * rbf_component)
        
        return scale_factor * total