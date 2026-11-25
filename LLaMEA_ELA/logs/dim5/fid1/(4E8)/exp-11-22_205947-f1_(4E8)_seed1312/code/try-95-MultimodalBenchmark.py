import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic parameters for phase modulation and coupling
        self.phase_shifts = np.linspace(0, 2*np.pi, dim, endpoint=False)
        self.coupling_strength = 0.5 + 0.3 * np.sin(np.arange(dim) * 0.7)
        self.sigmoid_params = 1.0 + 0.5 * np.cos(np.arange(dim) * 0.4)
        
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
            
        # Dynamic phase-shifted trigonometric terms with quaternion-inspired coupling
        phase_component = 0.0
        for i in range(self.dim):
            phase = self.phase_shifts[i]
            phase_component += np.sin(5.0 * x[i] + phase) * np.cos(7.0 * x[i] + phase)
            
        # Non-linear coupling with dynamic weights and quaternion-inspired terms
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = self.coupling_strength[i] * self.coupling_strength[j]
                # Quaternion-inspired coupling term
                quat_term = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                coupling_component += weight * (x[i]**2 + x[j]**2) * quat_term
                
        # Sharp multimodal peaks with adaptive scaling and sigmoidal modulation
        peak_component = 0.0
        for i in range(self.dim):
            # Multiple sharp peaks at different scales
            peak_component += (0.5 * np.exp(-0.5 * ((x[i] - 2.0)**2)) + 
                             0.3 * np.exp(-0.5 * ((x[i] + 2.0)**2)) + 
                             0.2 * np.exp(-0.5 * ((x[i] - 4.0)**2))) * \
                             (1.0 + 0.1 * np.sin(self.sigmoid_params[i] * x[i]))
        
        # Smooth radial basis with dynamic centers and adaptive widths
        rbf_component = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.5)
            width = 1.0 + 0.2 * np.cos(i * 0.3)
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Add quaternion-inspired high-order terms
        quaternion_component = 0.0
        for i in range(0, self.dim, 2):
            if i+1 < self.dim:
                quaternion_component += (x[i]**3 + x[i+1]**3) * np.sin(x[i] * x[i+1])
                
        # Combine all components with dimension-dependent scaling
        total = (0.3 * grad_component + 
                0.25 * phase_component + 
                0.2 * coupling_component + 
                0.15 * peak_component + 
                0.08 * rbf_component + 
                0.02 * quaternion_component)
        
        # Add a global scaling factor based on dimension
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        return scale_factor * total