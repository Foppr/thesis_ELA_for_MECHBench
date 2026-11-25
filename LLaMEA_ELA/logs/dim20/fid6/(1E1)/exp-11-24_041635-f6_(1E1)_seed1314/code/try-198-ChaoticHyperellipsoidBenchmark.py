import numpy as np

class ChaoticHyperellipsoidBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrices for different subspaces
        self.rotations = []
        for i in range(0, dim, 2):
            if i + 1 < dim:
                angle = np.pi * (i / dim) * 1.5
                c, s = np.cos(angle), np.sin(angle)
                self.rotations.append(np.array([[c, -s], [s, c]]))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperellipsoid components with rotation
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Extract 2D subspace
                xi = x[i:i+2]
                
                # Apply rotation
                rotated = self.rotations[(i // 2) % len(self.rotations)] @ xi
                
                # Hyperellipsoid term with varying exponents and altered coefficients
                a, b = 1.0 + i * 0.2, 1.0 + (i + 1) * 0.25
                term = (rotated[0] / a)**2.5 + (rotated[1] / b)**3.5
                
                # Add chaotic modulation with increased frequency and altered amplitude
                chaos = np.sin(20 * rotated[0]) * np.cos(15 * rotated[1]) * 0.6
                
                result += term + chaos
        
        # Additional chaotic sinusoidal components with higher frequencies and modified amplitudes
        for i in range(self.dim):
            freq = 4.0 + i * 0.5
            amp = 0.7 + i * 0.1
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.9)
        
        # Add a novel global modulation function with increased complexity
        r = np.sqrt(np.sum(x**2))
        global_mod = np.sin(0.5 * r) * np.cos(0.4 * r) * np.exp(-0.08 * r) * np.sin(0.3 * r)
        result += 0.5 * global_mod
        
        # Add a term that creates many local minima through irregular oscillations with new coefficients
        irregular = 0.0
        for i in range(self.dim):
            irregular += np.sin(25 * x[i]) * np.cos(20 * x[i]) * (1.0 + 0.2 * x[i]**2)
        result += 0.4 * irregular
        
        # Add enhanced cross-term interactions with increased coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * x[i] * x[j] * np.sin(7 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        
        # Add a novel interaction term that creates plateaus and sharp ridges
        plateau_term = 0.0
        for i in range(self.dim):
            plateau_term += np.sin(10 * x[i]) * np.cos(8 * x[i]) * (np.abs(x[i]) + 0.5)
        result += 0.25 * plateau_term
        
        return result