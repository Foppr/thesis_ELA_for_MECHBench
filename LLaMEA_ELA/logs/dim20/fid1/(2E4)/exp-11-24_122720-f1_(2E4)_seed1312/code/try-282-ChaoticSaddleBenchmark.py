import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.omega = [2.0 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.gamma = [0.1 + 0.05 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.fractal_dim = 1.5 + 0.2 * np.sin(dim * np.pi / 8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal basin component with chaotic saddle structure
        fractal = 0
        for i in range(self.dim):
            omega = self.omega[i]
            gamma = self.gamma[i]
            # Chaotic saddle potential with multi-scale oscillations
            saddle = np.sin(omega * x[i]) * np.cos(gamma * x[i]**2)
            fractal += saddle
            
        # Multi-scale oscillatory features
        oscillatory = 0
        for i in range(self.dim):
            scale = (i + 1) / self.dim
            # Multi-frequency sine waves with varying amplitudes
            freq1 = scale * 2 * np.pi
            freq2 = scale * 4 * np.pi
            freq3 = scale * 8 * np.pi
            oscillatory += (
                0.5 * np.sin(freq1 * x[i]) + 
                0.3 * np.sin(freq2 * x[i]) + 
                0.1 * np.sin(freq3 * x[i])
            )
            
        # Saddle point interaction terms with fractal scaling
        saddle_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                # Saddle point coupling with distance-dependent strength
                dist = np.abs(x[i] - x[j])
                coupling = np.exp(-dist * 0.5) * np.sin(x[i] + x[j])
                saddle_interaction += coupling
                
        # Fractal basin boundary modulation
        boundary_mod = 0
        for i in range(self.dim):
            # Boundary-sensitive term with fractal dimension scaling
            boundary_term = np.abs(x[i]) ** self.fractal_dim
            boundary_mod += boundary_term
            
        # Combine all components with proper weighting and global scaling
        result = 1.2 * fractal + 0.8 * oscillatory + 0.3 * saddle_interaction + 0.1 * boundary_mod
        
        # Add dimensionality-dependent scaling factor
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= scale_factor
        
        return result