import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic parameters for phase modulation and coupling
        self.phase_shifts = np.linspace(0, 2*np.pi, dim, endpoint=False)
        self.coupling_strength = 0.5 + 0.3 * np.sin(np.arange(dim) * 0.7)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with implicit constraint
        grad_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Implicit constraint via gradient modulation
            constraint_term = np.sin(xi) * np.cos(xi)
            grad_component += (xi**4 + 2*xi**3 + xi**2) * constraint_term
            
        # Dynamic phase-shifted trigonometric terms
        phase_component = 0.0
        for i in range(self.dim):
            phase = self.phase_shifts[i]
            phase_component += np.sin(5.0 * x[i] + phase) * np.cos(7.0 * x[i] + phase)
            
        # Non-linear coupling with dynamic weights
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = self.coupling_strength[i] * self.coupling_strength[j]
                coupling_component += weight * (x[i]**2 + x[j]**2) * np.sin(3.0 * (x[i] - x[j]))
                
        # Sharp multimodal peaks with adaptive scaling
        peak_component = 0.0
        for i in range(self.dim):
            # Multiple sharp peaks at different scales
            peak_component += 0.5 * np.exp(-0.5 * ((x[i] - 2.0)**2)) + \
                             0.3 * np.exp(-0.5 * ((x[i] + 2.0)**2)) + \
                             0.2 * np.exp(-0.5 * ((x[i] - 4.0)**2))
        
        # Smooth radial basis with dynamic centers
        rbf_component = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.5)
            width = 1.0 + 0.2 * np.cos(i * 0.3)
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Combine all components with dimension-dependent scaling
        total = (0.4 * grad_component + 
                0.3 * phase_component + 
                0.2 * coupling_component + 
                0.1 * peak_component + 
                0.05 * rbf_component)
        
        # Add a global scaling factor based on dimension
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        return scale_factor * total