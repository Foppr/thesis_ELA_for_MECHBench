import numpy as np

class ChaoticElasticPotentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Hyper-elastic component with exponential strain energy
        elastic_energy = 0.0
        for i in range(self.dim):
            # Nonlinear elastic response with varying stiffness
            stiffness = 2.0 + 1.5 * np.sin(0.5 * x_scaled[i])
            displacement = x_scaled[i]**2
            elastic_energy += stiffness * displacement * np.exp(-displacement)
        
        # Chaotic periodic component with multiple frequencies and modulations
        chaotic_periodic = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 0.8 * np.sin(x_scaled[i] * 0.7)
            freq2 = 1.5 + 0.6 * np.cos(x_scaled[i] * 0.9)
            modulation = 1.0 + 0.3 * np.sin(3.0 * x_scaled[i])
            chaotic_periodic += modulation * np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i])
        
        # Embedded fractal-like structure with recursive self-similarity
        fractal_structure = 0.0
        for i in range(self.dim):
            # Recursive pattern with diminishing amplitude
            for k in range(1, 6):
                amplitude = 1.0 / (k * k)
                frequency = k * 4.0 + 2.0 * np.sin(k * x_scaled[i])
                fractal_structure += amplitude * np.sin(frequency * x_scaled[i])
        
        # Discontinuous gradient regions with step-like transitions
        discontinuous = 0.0
        for i in range(self.dim):
            # Step function with varying transition points and heights
            step_point = np.sin(i * 0.5) * 0.8
            if x_scaled[i] < step_point:
                discontinuous += 2.0 * (step_point - x_scaled[i])**2
            else:
                discontinuous += 1.0 * (x_scaled[i] - step_point)**3
        
        # Cross-term interactions with higher-order polynomial coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Coupling with polynomial interaction and dimensionally varying strength
                coupling_strength = 1.2 + 0.5 * np.sin(i * 0.3) * np.cos(j * 0.4)
                cross_terms += coupling_strength * (x_scaled[i]**3) * (x_scaled[j]**2)
        
        # Combined function with carefully balanced weights
        return 1.2 * elastic_energy + 0.8 * chaotic_periodic + 0.6 * fractal_structure + 0.9 * discontinuous + 0.7 * cross_terms